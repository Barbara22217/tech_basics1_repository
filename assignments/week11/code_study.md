# Code Study: recipe.py from Model Bakery

##  Source
Repository: [model-bakers/model_bakery](https://github.com/model-bakers/model_bakery)  
File: [`recipe.py`](https://github.com/model-bakers/model_bakery/blob/main/model_bakery/recipe.py)

## Step by step explanation
import collections #this one imports collections, meaning that it gives the access to specialized data structures, like defaultdict for example, without the need to check if the key exists first. 
import copy #it provides functions to copy images, especially complex or nested ones. it is used to make sure each test data recipe is completely independent, which is especially important when sharing templates. 
import itertools #this gives tools for efficient looping and combinatorics. In this code it's used to create iterators that supply default values for fields when generating multiple objects at once.
from typing import ( #These imports bring in type hints from Python's typing module. They help developers (and editors/tools like Pyright or mypy) understand what kinds of inputs/outputs are expected.
    Any,
    Dict,
    Generic,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
    cast,
    overload,
)

from django.db.models import Model #This imports the base Model class from Django. Any model you define in Django (like User, Post, etc.) inherits from this.

#the four below import other parts of the same project (model_bakery):
from . import baker #Imports the baker.py module - this has the logic for building test model instances (like baker.make()).
from ._types import M #M is a type alias or generic type variable defined in _types.py.
from .exceptions import RecipeNotFound #Imports a custom exception that’s raised if someone tries to use a recipe that doesn't exist.
from .utils import ( 
    get_calling_module, #figures out which module is calling the code. Used for registering or loading recipes dynamically.
    seq, #a sequence helper (e.g., to assign increasing numbers to test data). # noqa: F401 - Enable seq to be imported from recipes #tells linters not to complain if seq is imported but unused - they keep it available for external use.
)

finder = baker.ModelFinder() #This creates an instance of ModelFinder, a class defined in baker.py.


class Recipe(Generic[M]): #This defines a generic class named Recipe which works with a Django model type M., Generic[M] means Recipe can be specialized for any model type M (where M is usually a subclass of django.db.models.Model).
    _T = TypeVar("_T", bound="Recipe[M]") #_T is a type variable used for typing methods like .extend() to return the same type as the class. Bound means _T can only be Recipe[M] or subclasses.

    def __init__(self, _model: Union[str, Type[M]], **attrs: Any) -> None: # Initializes the class Recipe with a model (string or class) and default attributes, and prepares internal storage for managing iterator-backed fields.
        self.attr_mapping = attrs  #Store default attribute values for the recipe
        self._model = _model  # Store the model class or model name (string)
        # _iterator_backups will hold values of the form (backup_iterator, usable_iterator).
        self._iterator_backups = {}  # type: Dict[str, Any] 

    def _mapping(  # noqa: C901
        self, _using: str, new_attrs: Dict[str, Any]
    ) -> Dict[str, Any]:
        _save_related = new_attrs.get("_save_related", True) # Whether to save related objects
        _quantity = new_attrs.get("_quantity", 1)  # Number of instances to create
# Extract related field attributes containing '__' (e.g., foreign key overrides)
        rel_fields_attrs = {k: v for k, v in new_attrs.items() if "__" in k}
 # Extract direct attributes excluding related field overrides
        new_attrs = {k: v for k, v in new_attrs.items() if "__" not in k}
        mapping = self.attr_mapping.copy()  # Start from default attributes
        for k, v in self.attr_mapping.items():
            # do not generate values if field value is provided
            if k in new_attrs:
 # If value is an iterator (like a sequence), handle unique value generation
                continue
            elif isinstance(v, collections.abc.Iterator):
 # Resolve model class if given as string
                if isinstance(self._model, str):
                    m = finder.get_model(self._model)
                else:
                    m = self._model
  # Initialize iterator backups if not present or if no objects exist in DB
                if k not in self._iterator_backups or not m.objects.exists():
                    self._iterator_backups[k] = itertools.tee(
                        self._iterator_backups.get(k, [v])[0]
                    )
                mapping[k] = self._iterator_backups[k][1] # Use usable iterator for this field
            # If value is a RecipeForeignKey (related model recipe)
            elif isinstance(v, RecipeForeignKey):
                attrs = {}
  # Separate related attrs for this foreign key (like "fk__field")
                # Remove any related field attrs from the recipe attrs before filtering
                for key, _value in list(rel_fields_attrs.items()):
                    if key.startswith(f"{k}__"):
                        attrs[key] = rel_fields_attrs.pop(key)
 # Filter related attrs specific to this foreign key
                recipe_attrs = baker.filter_rel_attrs(k, **attrs)
                if _save_related:
 # For one-to-one relations, create unique foreign keys per quantity
                    # Create a unique foreign key for each quantity if one_to_one required
                    if v.one_to_one is True:
                        rel_gen = [
                            v.recipe.make(_using=_using, **recipe_attrs)
                            for _ in range(_quantity)
                        ]
                        mapping[k] = itertools.cycle(rel_gen) # Cycle through unique related instances
                    # Otherwise create shared foreign key for each quantity
                    else:
 # For many-to-one, create one shared related instance for all quantity
                        mapping[k] = v.recipe.make(_using=_using, **recipe_attrs)
                else:
 # If not saving related objects, prepare unsaved related instances
                    mapping[k] = v.recipe.prepare(_using=_using, **recipe_attrs)
 # If value is a related object handler, call its make method
            elif isinstance(v, related):
                mapping[k] = v.make
 # For containers like lists or dicts, deep copy to avoid shared mutable state
            elif isinstance(v, collections.abc.Container):
                mapping[k] = copy.deepcopy(v)

        mapping.update(new_attrs) # Override with any explicitly passed attributes
        mapping.update(rel_fields_attrs) # Add any related field overrides
        return mapping # Return final attribute dict for instance creation

    @overload #@overload is a typing-only decorator provided by Python’s typing module. It is used to define multiple type signatures for the same function to help static type checkers (like mypy or PyCharm) understand how the return type depends on the input parameters.
#It's not actually run at runtime — it’s only for tools and editors to understand your code better.
    def make(
        self,
        _quantity: None = None,
        make_m2m: bool = False,
        _refresh_after_create: bool = False,
        _create_files: bool = False,
        _using: str = "",
        _bulk_create: bool = False,
        _save_kwargs: Optional[Dict[str, Any]] = None,
        **attrs: Any,
    ) -> M: ...
#make() function has two overloads, the first one Means: If _quantity is None, then return a single object of type M. the second one Means: If _quantity is an int, then return a list of objects of type M.
    @overload
    def make(
        self,
        _quantity: int,
        make_m2m: bool = False,
        _refresh_after_create: bool = False,
        _create_files: bool = False,
        _using: str = "",
        _bulk_create: bool = False,
        _save_kwargs: Optional[Dict[str, Any]] = None,
        **attrs: Any,
    ) -> List[M]: ...
# It’s a clean way to let type checkers know: that this method can return one or many depending on how you call it.

    def make(
        self,
        _quantity: Optional[int] = None,
        make_m2m: Optional[bool] = None,
        _refresh_after_create: Optional[bool] = None,
        _create_files: Optional[bool] = None,
        _using: str = "",
        _bulk_create: Optional[bool] = None,
        _save_kwargs: Optional[Dict[str, Any]] = None,
        **attrs: Any,
    ) -> Union[M, List[M]]:
#so, the part above creates a method "make" method that takes various optional flags and any additional attributes. These control how many objects to create, whether to create related objects (like many-to-many), use bulk creation, etc. **attrs: catch-all for any model fields you want to override (like name="Alice").
        defaults = {} #Initializes a dictionary to collect options for object creation.
        if _quantity is not None: #If the user asked to create multiple instances (_quantity), add it to defaults.
            defaults["_quantity"] = _quantity
        if make_m2m is not None:
            defaults["make_m2m"] = make_m2m
        if _refresh_after_create is not None:
            defaults["_refresh_after_create"] = _refresh_after_create
        if _create_files is not None:
            defaults["_create_files"] = _create_files
        if _bulk_create is not None:
            defaults["_bulk_create"] = _bulk_create
        if _save_kwargs is not None:
            defaults["_save_kwargs"] = _save_kwargs  # type: ignore[assignment]
#the rest of if statements are all additional options passed to baker.make().
        defaults.update(attrs) #Merge any custom field values provided by the user (e.g., name="Bob").
        return baker.make(self._model, _using=_using, **self._mapping(_using, defaults)) #Calls baker.make() to create one or more model instances. self._model: the Django model class to use._using: lets you choose a database (if you're using multiple).**self._mapping(...): generates the final attributes for the model using the recipe logic, including foreign keys, iterators, and more.

    @overload
    def prepare(
        self,
        _quantity: None = None,
        _save_related: bool = False,
        _using: str = "",
        **attrs: Any,
    ) -> M: ...

    @overload
    def prepare(
        self,
        _quantity: int,
        _save_related: bool = False,
        _using: str = "",
        **attrs: Any,
    ) -> List[M]: ...
#these two overloads are just for the type checkers, and they are skipped at runtime
    def prepare(
        self,
        _quantity: Optional[int] = None,
        _save_related: bool = False,
        _using: str = "",
        **attrs: Any,
    ) -> Union[M, List[M]]:
        defaults = { #Start with a single option: whether to prepare related models
            "_save_related": _save_related,
        }
        if _quantity is not None: #If the user wants multiple instances, include that in the defaults
            defaults["_quantity"] = _quantity  # type: ignore[assignment]
#this block above is the real method, with parameters: _quantity: how many instances to prepare, _save_related: whether to recursively prepare related fields (foreign keys, etc.)_using: which DB alias to use (for multi-database support) **attrs: any field values to override


        defaults.update(attrs) #Add in any field values passed directly (like name="Alice")
        return baker.prepare( #this prepares the instances, Call baker.prepare() (from model_bakery) Uses:self._model: the model class or name**self._mapping(...): attributes merged from the recipe and overrides. This returns:A single model instance, or A list of model instances (depending on _quantity)


            self._model, _using=_using, **self._mapping(_using, defaults)
        )

    def extend(self: _T, **attrs: Any) -> _T:
        attr_mapping = self.attr_mapping.copy() Make a copy of the current recipe's attribute mapping (so we don't modify the original)
        attr_mapping.update(attrs) #Update the copied mapping with any new or overridden attributes provided
        return type(self)(self._model, **attr_mapping) #Return a new instance of the same Recipe class, with: The same model (self._model) The updated attribute mapping

# This function below loads a recipe object by name (string) from the calling module - i.e., the file where the function was called.
def _load_recipe_from_calling_module(recipe: str) -> Recipe[Model]: 
    """Load `Recipe` from the string attribute given from the calling module.

    Args:
        recipe (str): the name of the recipe attribute within the module from
            which it should be loaded

    Returns:
        (Recipe): recipe resolved from calling module
    """
    recipe = getattr(get_calling_module(2), recipe) #Uses getattr() to find the variable with the given name (recipe) in the calling module get_calling_module(2) gets the caller's module, 2 levels up in the call stack
    if recipe:
        return cast(Recipe[Model], recipe) #If the attribute exists, cast it to the expected type (Recipe[Model]) and return it
    else:
        raise RecipeNotFound #If it doesn't exist, raise a custom RecipeNotFound exception


class RecipeForeignKey(Generic[M]): #this is another class, named Recipe Foreign Key
    """A `Recipe` to use for making ManyToOne and OneToOne related objects."""

    def __init__(self, recipe: Recipe[M], one_to_one: bool) -> None: #here it initializes method inside this class, with objects recipe and one_to_one
        if isinstance(recipe, Recipe):
            self.recipe = recipe
            self.one_to_one = one_to_one
        else:
            raise TypeError("Not a recipe")


def foreign_key( #another function, here outside the class
    recipe: Union[Recipe[M], str], one_to_one: bool = False
) -> RecipeForeignKey[M]:
    """Return a `RecipeForeignKey`.

    Return the callable, so that the associated `_model` will not be created
    during the recipe definition.

    This resolves recipes supplied as strings from other module paths or from
    the calling code's module.
    """
    if isinstance(recipe, str):
        # Load `Recipe` from string before handing off to `RecipeForeignKey`
        try:
            # Try to load from another module
            recipe = baker._recipe(recipe)
        except (AttributeError, ImportError, ValueError):
            # Probably not in another module, so load it from calling module
            recipe = _load_recipe_from_calling_module(cast(str, recipe))

    return RecipeForeignKey(cast(Recipe[M], recipe), one_to_one)


class related(Generic[M]):  # FIXME #anotherclass
    def __init__(self, *args: Union[str, Recipe[M]]) -> None:
        self.related = []  # type: List[Recipe[M]]
        for recipe in args:
            if isinstance(recipe, Recipe):
                self.related.append(recipe)
            elif isinstance(recipe, str):
                recipe = _load_recipe_from_calling_module(recipe)
                if recipe:
                    self.related.append(recipe)
                else:
                    raise RecipeNotFound
            else:
                raise TypeError("Not a recipe")

    def make(self) -> List[Union[M, List[M]]]:
        """Persist objects to m2m relation."""
        return [m.make() for m in self.related]

