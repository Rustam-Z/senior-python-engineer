# Design Patterns with Python

### Types of design patterns
- Creational - designed for object creation to increase flexibility and reuse of existing code. Polymorphism is used.
- Structural - establishes relationship between classes making larger structures. Inheritance is used.
- Behavioral - effective communications and interactions between objects. Methods are used.

### Using common design patterns, you can:
- Speed up the development process;
- Reduce the number of lines of code;
- Make sure your code is well-designed;
- Anticipate future problems arising from small issues.

## Notes
1. Creational
   - [Factory](c_factory/factory.py), factory method is a single method.
   - [Factory abstract](c_factory/abstact_factory.py), an abstract factory is an object.
   - [Singleton](c_singleton/singleton.py), object creating from class, global variable in an object-oriented way. Borg. Sharing info by multiple objects.
   - [Builder](c_builder/builder.py), separating class from building complex object.
   - [Prototype](c_prototype/prototype.py), clones object.
2. Structural
   - [Decorator](s_decorator/decorator.py), adds new features to existing objects without changing their structures,
   - [Proxy](s_proxy/proxy.py), becomes handy when creating resource-intensive objects.
   - [Adapter](s_adapter/adapter.py), converting the interface of a class into another one that a client is expecting.
     - Making the incompatible objects adaptable to each other.
   - [Composite](s_composite/composite.py), describes a group of objects the same way as a single instance, with Tree data structure.
   - [Bridge](s_bridge/bridge.py), separate the Implementation Specific Abstractions and Implementation Independent Abstractions.
     - Adapter vs bridge? 
     - Adapter is used to map that interface to another object which has similar functional role, but a different interface.
     - You have designed all your classes, Bridge is used when you need to be able to swap out different implementations.
     - It is also similar to Abstract Factory pattern. In Bridge, abstraction and implementation will vary independently. But in abstract factory, if you change abstraction ( interface), you have to change client.
   - Facade, flyweight
3. Behavioural
   - [Iterator](b_iterator/iterator.py), helps to iterate through the elements of collection.
   - [Observer](b_observer/observer.py), lets subscribed entities know about changes in an observable. Ex: Elon & Twitter.
   - [Strategy](b_strategy/strategy.py), enables our application to select algorithms (method) at runtime.
   - [Visitor](b_visitor/visitor.py), new features to an existing hierarchy without changing its structure. Ex: electricity, hvac.
   - [Chain of responsibility](b_chain_of_responsibility/chain_of_responsibility.py), allows a request to pass down a chain of receivers until it is handled.


## Resources
- https://www.linkedin.com/learning/python-design-patterns/welcome?u=2113185
- https://github.com/faif/python-patterns
- https://jellyfish.tech/implementation-of-common-design-patterns-in-python/
- https://python-patterns.guide
- https://www.toptal.com/python/python-design-patterns
