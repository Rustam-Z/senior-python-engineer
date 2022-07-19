# Python S.O.L.I.D Principles - Create more classes

### Why follow SOLID?
- Use SOLID principles to address design deficiencies
- Some problems without SOLID
  - Mixed responsibility 
  - Missing responsibility
  - Limited reuse potential
  - Not substitutable

### S.O.L.I.D - Order doesn't matter
1. Interface segregation 
   1. Helps design good classes
   2. Helps write unit test cases
2. Liskov substitution - how subclasses extend superclasses
   1. Object of superclass S can be replaced with objects of any subclass of S
   2. Helps design good polymorphism
3. Open/closed - tuning the design
   1. Open to extension means adding subclasses a needed
   2. Closed to modification avoids "tweaking" the code to handle new situations
4. Dependency inversion - based on packaging the code
   1. A direct dependency on a concrete class needs to be "inverted"
   2. Depend on abstraction classes
   3. Avoid concrete class name dependencies
5. Single responsibility - summary of other 4 principles
   1. One responsibility per class
   2. "A class should have one reason to change"
   3. Note!! "Single" at what level of abstraction? How are the responsibilities counter?

### Other OO Principle
- Don't repeat yourself (DRY)
- General responsibility assignment software principles (GRASP)
- Test-driven development (TDD)

## Resources
- https://github.com/heykarimoff/solid.python/
- https://www.linkedin.com/learning/learning-s-o-l-i-d-programming-principles
- https://www.pythontutorial.net/python-oop/python-single-responsibility-principle/
