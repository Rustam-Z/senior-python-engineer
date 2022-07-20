# Design Patterns with Python

### Types of design patterns
- Creational - designed for object creation to increase flexibility and reuse of existing code. Polymorphism is used.
- Structural - establishes relationship between classes making larger structures. Inheritance is used.
- Behavioral - effective communications and interactions between objects/classes. Methods are used.

### Using common design patterns, you can:
- Speed up the development process;
- Reduce the number of lines of code;
- Make sure your code is well-designed;
- Anticipate future problems arising from small issues.

## Notes
1. Creational
   - [Singleton](c_singleton/singleton.py), restricts a class from having more than one instance and ensures a global access point to this instance.
   - [Borg](c_singleton/borg.py), allows all instances of one class share common data.
   - [Factory](c_factory/factory.py), the object helps to create other objects.
   - [Factory abstract](c_factory/abstact_factory.py), like factory but abstract factory is an object.
   - [Builder](c_builder/builder.py), separating class from building complex object.
   - [Prototype](c_prototype/prototype.py), clones object.
   - [Pool](c_pool/pool.py), like flyweight but for mutable objects
3. Structural
   - [Facade](s_facade/facade.py), hides the complexity of implementations. New API on top of other APIs.
   - [Decorator](s_decorator/decorator.py), attaches new behaviors to the objects without modifying their structure.
   - [Adapter](s_adapter/adapter.py), makes incompatible objects adaptable to each other. Ex: `speak=english.hello(), speak=korean.anyong()`
   - [Bridge](s_bridge/bridge.py), separates the implementation from the API. Ex: DrawingAPIOne, DrawingAPITwo
   - [Proxy](s_proxy/proxy.py), like decorator, adds functionality to a class without  changing its interface.
   - [Composite](s_composite/composite.py), describes a group of objects the same way as a single instance, with Tree data structure.
   - [Flyweight](s_flyweight/flyweight.py), reuses existing instances of objects with similar/identical state.
4. Behavioural
   - [Iterator](b_iterator/iterator.py), helps to iterate through the elements of collection.
   - [Observer](b_observer/observer.py), lets subscribed entities know about changes in an observable. Ex: Elon & Twitter.
   - [Strategy](b_strategy/strategy.py), enables our application to select algorithms (method) at runtime.
   - [Visitor](b_visitor/visitor.py), adds new features to an existing hierarchy without changing its structure. Ex: electricity, hvac.
   - [Mediator](b_mediator/mediator.py), objects in a system communicate through a Mediator instead of directly with each other.
   - [Chain of responsibility](b_chain_of_responsibility/chain_of_responsibility.py), allows a request to pass down a chain of receivers until it is handled.


## Resources
- https://www.linkedin.com/learning/python-design-patterns/welcome?u=2113185
- https://github.com/faif/python-patterns
- https://jellyfish.tech/implementation-of-common-design-patterns-in-python/
- https://python-patterns.guide
- https://www.toptal.com/python/python-design-patterns
