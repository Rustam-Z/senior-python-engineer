# Design Patterns with Python
Design patterns are the best-formalized practices a programmer can use to solve common problems when designing an application or system.

### Types of design patterns
- Creational - designed for object creation to increase flexibility and reuse of existing code. Polymorphism is used.
- Structural - establishes a relationship between classes making larger structures. Inheritance is used.
  - Whenever you think of designing architecture for your system, structural design patterns help you to plan for the future, and arrange classes in neat hierarchies.
- Behavioral - effective communications and interactions between objects/classes. Methods are used.

### Using common design patterns, you can:
- Speed up the development process;
- Reduce the number of lines of code;
- Make sure your code is well-designed;
- Anticipate future problems arising from small issues.

## Notes
1. Creational
   - *[Singleton](c_singleton/singleton.py), restricts a class from having more than one instance and ensures a global access point to this instance.
   - *[Factory](c_factory/factory.py), the method that helps to create other objects.
   - *[Factory abstract](c_factory/abstact_factory.py), like factory but object that provides a way to encapsulate a group of individual factories.
   - *[Builder](c_builder/builder.py), separating class from building complex object.
   - [Borg](c_singleton/borg.py), allows all instances of one class to share common data.
   - [Prototype](c_prototype/prototype.py), registers object and clones objects (if instantiation is costly).
   - [Pool](c_pool/pool.py), like flyweight but for mutable objects.
3. Structural
   - *[Facade](s_facade/facade.py), hides the complexity of implementations. New API on top of other APIs.
   - *[Bridge](s_bridge/bridge.py), separates the implementation from abstraction. Ex: DrawingAPIOne, DrawingAPITwo
   - *[Adapter](s_adapter/adapter.py), makes incompatible objects adaptable to each other. Ex: `speak=english.hello(), speak=korean.anyong()`
   - *[Proxy](s_proxy/proxy.py), like decorator, adds functionality to a class without changing its interface.
   - [Decorator](s_decorator/decorator.py), attach new behaviors to the objects without modifying their structure.
   - [Composite](s_composite/composite.py), describes a group of objects the same way as a single instance, using a Tree data structure.
   - [Flyweight](s_flyweight/flyweight.py), cache, reuses existing instances of objects with similar/identical state.
4. Behavioural
   - *[Strategy](b_strategy/strategy.py), enables our application to select algorithms (method) at runtime.
   - *[Observer](b_observer/observer.py), lets subscribed entities know about changes in an observable. Ex: Elon & Twitter.
   - *[Iterator](b_iterator/iterator.py), helps to iterate through the elements of the collection.
   - *[Mediator](b_mediator/mediator.py), objects in a system communicate through a Mediator instead of directly with each other.
   - [Publish & Subscribe](b_publish_subscribe/publish_subscribe.py), a source syndicates events/data to 0+ registered listeners.
   - [Visitor](b_visitor/visitor.py), adds new features to an existing hierarchy without changing its structure. Ex: electricity, hvac.
   - [Chain of responsibility](b_chain_of_responsibility/chain_of_responsibility.py), allows a request to pass down a chain of receivers until it is handled.
   - [Template](b_template/template.py), defines the skeleton of a base algorithm, deferring the definition of exact steps to subclasses.
   - Momento, generates an opaque token that can be used to go back to a previous state.
   - State, logic is organized into a discrete number of potential states and the next state that can be transitioned to

## Resources
- By NeetCode https://youtu.be/tAuRQs_d9F8
- By Fireship https://youtu.be/tv-_1er1mWI
- https://www.linkedin.com/learning/python-design-patterns/welcome?u=2113185
- https://github.com/faif/python-patterns
- https://jellyfish.tech/implementation-of-common-design-patterns-in-python/
- https://youtube.com/playlist?list=PLO6785UZapFX5bO4ZZSO7Unn2uOTNFqfQ
- https://www.toptal.com/python/python-design-patterns
- https://python-patterns.guide
