# Design Patterns with Python

1. Creational - designed for class instantiation. Polymorphism is used.
    - [Factory](factory/factory.py), factory method is a single method.
    - [Factory abstract](factory/abstact_factory.py), an abstract factory is an object.
    - [Singleton](singleton/singleton.py), object creating from class, global variable in an object-oriented way. Borg. Sharing info by multiple objects.
    - [Builder](builder/builder.py), separating class from building complex object.
    - [Prototype](prototype/prototype.py), clones object.
2. Structural - to establish relationship between software components, accomplish functional (what it should do) and non-functional requirements (how when it does the work). Inheritance is used.
    - [Decorator](decorator/decorator.py), adds new features to existing objects without changing their structures,
    - [Proxy](proxy/proxy.py), becomes handy when creating resource-intensive objects.
    - [Adapter](adapter/adapter.py), converting the interface of a class into another one that a client is expecting.
      - Making the incompatible objects adaptable to each other.
    - [Composite](composite/composite.py), describes a group of objects the same way as a single instance, with Tree data structure.
    - [Bridge](bridge/bridge.py), separate the Implementation Specific Abstractions and Implementation Independent Abstractions.
      - Adapter vs bridge? 
      - Adapter is used to map that interface to another object which has similar functional role, but a different interface.
      - You have designed all your classes, Bridge is used when you need to be able to swap out different implementations.
      - It is also similar to Abstract Factory pattern. In Bridge, abstraction and implementation will vary independently. But in abstract factory, if you change abstraction ( interface), you have to change client.
3. Behavioural - object interaction, these patterns are designed depending on how one class communicates with others. Methods are used.
    - [Observer](observer/observer.py), one subject monitored by many observers.
    - [Visitor](visitor/visitor.py), new features to an existing hierarchy without changing its structure.
    - [Iterator](iterator/iterator.py), iterating or traversing through the object.
    - [Strategy](strategy/strategy.py), we have a default method, we can change its behaviour with another function at a run time.
    - [Chain of responsibility](chain_of_responsibility/chain_of_responsibility.py), 

## Resources
- https://www.linkedin.com/learning/python-design-patterns/welcome?u=2113185
- https://github.com/faif/python-patterns
- https://www.tutorialspoint.com/python_design_patterns/index.htm
- https://www.youtube.com/watch?v=4KZx8bATBFs
- https://python-patterns.guide
- https://www.toptal.com/python/python-design-patterns
- https://jellyfish.tech/implementation-of-common-design-patterns-in-python/
