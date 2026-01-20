# S.O.L.I.D Principles

### Why follow SOLID?
- Some problems without SOLID
  - Mixed responsibility 
  - Missing responsibility
  - Limited reuse potential
  - Not substitutable
  - Not extensible, not scalable 

### S.O.L.I.D 
1. Interface segregation 
   1. Clients should not be forced to depend on methods they do not use. Helps design good classes.
   2. ISP is about making interfaces small so you don't force classes to do things they don't want to do.
   3. Helps write unit test cases.
   4. Example:
      - Bad: An interface `LibraryActions` that has `checkoutBook()`, `returnBook()`, and `rebindHardcover()`. A "Regular Member" class is forced to implement `rebindHardcover()` even though they aren't allowed to fix books.
      - Good: Split the interface. Use `BorrowerActions` for members and `MaintenanceActions` for the librarian.
2. Liskov substitution
   1. Subtypes must be substitutable for their base types. How subclasses extend superclasses. 
   2. LSP is about maintaining the "Contract": It ensures that a subclass doesn't break the expectations set by its parent. It’s the rule that allows you to use Polymorphism safely.
   3. Liskov substitution = interface segregation + polymorphism
   4. Example:
      - Bad: You have a base class `Bird` with a `fly()` method. You create a subclass `Ostrich`. Since an ostrich can't fly, you make `fly()` throw an error. Now, any code expecting a `Bird` might crash if it gets an `Ostrich`.
      - Good: Only put `fly()` in a `FlyingBird` subclass. The `Ostrich` should only inherit from a more general `Bird` class that doesn't assume flight.
   5. Another example:
      - The Violation: You have a `PhysicalBook` class with a method `getShelfLocation()`. You create a subclass `EBook`. Since an E-Book doesn't have a shelf, you make `getShelfLocation()` return null or throw an Error.
      - Why it's bad: If a `Librarian` object loops through a list of `Books` and calls `getShelfLocation()`, the code will crash or fail unexpectedly when it hits the E-Book.
      - The Fix: Don't put "Physical" properties in the base `Book` class.
3. Open/closed 
   1. Software entities should be open for extension, but closed for modification. Open for extension means adding subclasses when needed. Closed to modification avoids "tweaking" the code to handle new situations.
   2. OCP is about making code **extensible** so you never have to change your "core" logic when requirements change.
   3. Example:
      - Bad: You have a `Discount` class with a method `apply(book)`. Every time you add a new discount type (Student, Senior, Black Friday), you have to go inside the apply method and add an `if/else` block.
      - Good: Create a `Discount` interface. Each new discount type becomes its own class (`StudentDiscount`, `BlackFridayDiscount`). You can add 100 new discounts without ever touching the original code.
4. Dependency inversion 
   1. Depend on abstraction classes. Avoid concrete class name dependencies. A direct dependency on a concrete class needs to be "inverted"
   2. Example:
      - Bad: A `NotificationService` class that creates a new `EmailSender()` inside its constructor. The notification service is now "stuck" with email. It can't send SMS without a code rewrite.
      - Good: The `NotificationService` should ask for a `MessageSender` interface. You can then "inject" an `EmailSender`, `SmsSender`, or `WhatsAppSender` at runtime.
5. Single responsibility 
   1. One responsibility per class. A class should have only one reason to change.
   2. Example:
      - Bad: A `Book` class that holds data (title, author) and also handles saving the book to a database. If the database schema changes, you have to change the `Book` class.
      - Good: Use two classes: `Book` for the data and `BookRepository` for the database logic.

### Other Object Oriented Principle
- Use Composition (has-a) over Inheritance (is-a) whenever necessary.
  - Composition keeps classes independent. Use Inheritance when you want to achieve true Polymorphism: If you need to treat a group of different objects as the exact same type in a list or function.
- Don't repeat yourself (DRY)
  - Every piece of knowledge or logic must have a single, unambiguous representation within a system. If you are copy-pasting code, you should probably move that logic into a function or a shared component (Composition).
- KISS (Keep it simple): avoid "over-engineering." Don't implement a complex Factory Pattern if a simple if statement will work for the foreseeable future.
- Law of Demeter (The Principle of Least Knowledge). A module should not know about the inner workings of the objects it manipulates.
  - `Bad: paperboy.customer.wallet.takeMoney()` (The paperboy is reaching into the customer's wallet).
  - `Good: customer.pay(paperboy)` (The paperboy asks the customer, and the customer handles their own wallet).
- General responsibility assignment software principles (GRASP)

## Resources
- https://github.com/heykarimoff/solid.python/
- https://www.linkedin.com/learning/learning-s-o-l-i-d-programming-principles
- https://www.pythontutorial.net/python-oop/python-single-responsibility-principle/
- https://www.linkedin.com/pulse/solid-what-do-you-need-know-fred-peixoto-aovmf/?utm_source=share&utm_medium=member_android&utm_campaign=share_via
