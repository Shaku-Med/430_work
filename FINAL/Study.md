# CSC430 Software Engineering Study Guide

## Key Concepts from Quizzes (Spring 2025)

### Basic Terminology

- **Tasks** are statements that define or qualify what a program needs to do.
- **Requirements** are statements that constrain the ways in which the software can be designed and implemented.
- **Lack of Communication** is one of the two major examples of growth in depth of complexity.
- **User Interface** is an interface with graphical icons to communicate to users.
- The **Task** qualify the functional requirements and specify in what manner they need to be achieved.

### Software Testing Concepts

- In **Black Box** testing, the test cases are based only on the requirements specification, not on the implementation code.

### Project Management Facts

- The final deadline for delivering the project does **NOT** come from the programmers because they know how long it will take to finish. (This is false)
- You should **NOT** implement every function, especially if the needed function exists in the standard library. (The correct answer is False)
- The program done in this chapter **IS** tested (String Sorter). (The correct answer is False)
- The time estimation for a development task should **NOT** be done by the client. (The correct answer is False)

### Code Review Benefits

- Showing your code to other people will:
  - **Help you find your defects**
  - Be a software review of your code
  - NOT be considered cheating in the academic world

### Software Complexity

- The amount of functionality, components, interfaces, and so on of the software refers to the **breadth** of software complexity.
- CI/CD stands for **Continuous Integration/Continuous Deployment**
- The term software engineering was first introduced in the year **1968** at the NATO conference in Germany to mimic the existing, traditional engineering disciplines.
- Frequent communication, simplicity in design and code, and feedback are three core values of **DevOps** programming.
- Main disadvantage of the Spiral Process model is **Low Complexity Management**

### Software Engineering Practices

- While Continuous Integration has been practiced since the 1970s, Continuous Integration and Continuous Deployment is a more recent practice. (**True**)
- The numbers of failures in software projects and defects encountered in the software products are **NOT** very few. (The statement "The numbers of failures in software projects and defects encountered in the software products are very few" is **False**)
- Software engineering is a broad field that touches upon all aspects of developing and supporting a software system. (**True**)
- Agile methods prefer **adapting to the people** over rigid processes. (The statement "Agile methods prefer rigid processes over adapting to the people" is **False**)
- There is **NOT** only one software engineering process model that fits each software project. (The statement "There is only one software engineering process model that fits each software project" is **False**)
- DevOps does **NOT** extend CI/CD to include IT Operations and Support. (The statement "DevOps extends CI/CD to include IT Operations and Support" is **False**)

### Technical Issues in Software Development

- Technical concerns in developing large systems can involve:
  - **The network**
  - Other concerns include: the database, version and configuration control

### Software Engineering Techniques

- A technique to "lessen" the relationships, number of functionalities, amount of interactions, and so on is **Integration** (although this may be incorrect - typically decomposition and modularization are used)

### Project Failure Reasons

- The main reasons projects were canceled, as uncovered by the Chaos report, are:
  - **Lack of resources and proper planning**

### Agile Processes

- Disadvantages of Agile processes include:
  - **Low process complexity**
- Advantages of agile processes include:
  - **Efficient handling of changes**
- Extreme programming practices writing test cases **before** writing the code.

### Software Architecture

- A system can be decomposed into different main modules. Each main module can be decomposed into smaller submodules. This decomposition can continue until the submodule is simple to design. (**True**)
- Service-Oriented Architecture (SOA) is an architectural style in which the architecture is divided into independent services, which are accessed only through the network. (**True**)
- Pre-condition is a condition that should be true if your module worked. (**False** - it should be true before the module executes)
- Programming libraries are not designed for reuse. (**False** - they are specifically designed for reuse)
- The CUPID principles completely replace SOLID, making SOLID principles obsolete in modern software development. (**False** - CUPID complements rather than replaces SOLID)
- In MVC, the Model is aware of the View and can directly communicate with it. (**True** - although traditional MVC often has the View observe the Model, not vice versa)

### REST Architecture

- The REST architecture is a:
  - **Style or pattern**

### Software Process Models

- **Waterfall**: A linear and sequential approach where each phase must be completed before moving to the next. (**E**)
- **Spiral**: A risk-driven model that combines iterative development with elements of prototyping. (**A**)
- **Incremental**: A method that builds the system in small parts, each adding functionality until completion. (**F**)
- **Scrum**: A framework that emphasizes teamwork, sprints, and iterative development with daily stand-ups. (**C**)
- **Agile**: A flexible and iterative approach that prioritizes customer collaboration and adaptability. (**D**)
- **XP**: A methodology that focuses on continuous feedback, pair programming, and test-driven development. (**B**)
- **DevOps**: A culture and practice that integrates development and operations for continuous delivery and automation. (**G**)

## Expected Exam Questions

1. **What is the difference between tasks and requirements in software engineering?**
   - Tasks define what a program needs to do, while requirements constrain how it can be designed and implemented.

2. **Explain the concept of black box testing and its importance.**
   - Black box testing focuses on testing based on requirements specifications without knowledge of the internal code, ensuring the software meets user requirements.

3. **What are the main advantages and disadvantages of the Agile development methodology?**
   - Advantages: Efficient handling of changes, customer collaboration, adaptability
   - Disadvantages: Low process complexity, may lack documentation, not ideal for all project types

4. **Compare and contrast Waterfall and Spiral process models.**
   - Waterfall is linear and sequential, while Spiral is risk-driven and combines iterative development with prototyping elements.

5. **What is the significance of CI/CD in modern software development?**
   - CI/CD (Continuous Integration/Continuous Deployment) automates the building, testing, and deployment process, leading to faster delivery and higher quality software.

6. **How does DevOps differ from traditional development approaches?**
   - DevOps integrates development and operations teams, focusing on automation, continuous delivery, and collaboration throughout the software lifecycle.

7. **Explain the concept of SOLID principles and their importance in software design.**
   - SOLID (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) provides guidelines for creating maintainable and scalable software systems.

8. **What is the purpose of software architecture patterns like MVC and REST?**
   - Architecture patterns provide proven solutions to common design problems, separating concerns and improving maintainability.

9. **Why is code review important in the software development process?**
   - Code reviews help find defects, share knowledge, ensure code quality, and maintain coding standards across the team.

10. **What are the main factors that contribute to software project failures?**
    - Lack of resources and proper planning, incomplete requirements, lack of user involvement, and poor communication are common factors.

11. **How do you estimate the time required for a software development task?**
    - Time estimation involves breaking down tasks, considering complexity, using historical data, and consulting with the development team.

12. **What is the role of testing in software development, and what are different types of testing?**
    - Testing verifies software quality and includes unit testing, integration testing, system testing, and acceptance testing.

## Note for Exam Preparation

Focus on understanding the concepts rather than memorizing definitions. Pay special attention to:
- Software process models and their characteristics
- Agile methodologies and principles
- Testing approaches and their importance
- Factors affecting software quality and project success
- Modern development practices (CI/CD, DevOps)
- Software architecture concepts and patterns

Remember to review all quiz materials thoroughly and practice explaining concepts in your own words.



### Software Design & Architecture

- Designing how to represent the data required for the software system and how to store it efficiently is part of **all of these**: Detail design, Database design, and Requirement design.

- The difference between Service-Oriented and Microservices architectures is:
  - **SOA does not support reusability, while Microservices are designed for maximum code reuse**
  - (Note: Other differences include: Microservices are typically smaller in scope/size, and Microservices typically use an Enterprise Service Bus while SOA services communicate directly)

- The primary difference between architectural design and detailed design in software engineering:
  - **Architectural design establishes the high-level structure and components of a system, while detailed design specifies the internal logic and algorithms**

- The Open/Closed Principle (OCP) states:
  - **Classes should be open for extension but closed for modification**
  - (Not "A class should always be publicly accessible" or "A class should never be extended or modified")

- For best design we want to achieve strong cohesion and tight coupling, with strong cohesion referring to how well-focused a module's responsibilities are, and tight coupling referring to how independent modules are from each other.

### Basic Terminology

- **Tasks** are statements that define or qualify what a program needs to do.
- **Requirements** are statements that constrain the ways in which the software can be designed and implemented.
- **Lack of Communication** is one of the two major examples of growth in depth of complexity.
- **User Interface** is an interface with graphical icons to communicate to users.
- The **Task** qualify the functional requirements and specify in what manner they need to be achieved.

### Agile and Development Roles

- When a software release is repeatedly failing in production due to untested features, the **Scrum Master** should ensure that testing is properly integrated into the development process.

- A development team struggling with poor code quality and frequent technical debt means the **Tech Lead** is primarily responsible for setting coding standards and guiding technical decisions.

### Code Quality & Testing

- What is the best type of comment to have in your code? **Explanation of the code**

- The four phases of debugging are: **Reproduction, Localization, Verification, Report**

- Boundary value analysis focuses on: **Examining values at the limit, just under, and just over**

- A software "build" is best described as: **A set of activities associated with the integration and conversion of source files to a set of executable files**

- Artifacts that are not related to each other: **User-interface screens and code segments**

- What is not a candidate for multithreading: **Usage of a Log file**

### Concurrency & Multithreading

- What is true about multithreaded environment: **Threads are always executed in parallel**

- The difference between concurrency and parallelism:
  - **Concurrency is about dealing with many things at once (structuring code to handle multiple tasks), while parallelism is about doing many things at once (executing multiple tasks simultaneously)**

- The primary purpose of using an API (Application Programming Interface) in a software application:
  - **To enable communication between different software systems or components by providing predefined functions and protocols**

### Software Quality & Testing

### Object Relationships

- The best kind of relationship the following objects should have: Bicycle/Wheels and Bicycle/Frame Parts? **Dependency and Realization**

### Design Patterns

- **Singleton** pattern: Ensuring that only one instance of a class exists in an application, such as a configuration manager.

- **Facade** pattern: Converting an interface of one class into another that a client expects.

- **Builder** pattern: Constructing complex objects step by step, such as assembling a meal order in a restaurant system.

- **Strategy** pattern: Defining a family of interchangeable algorithms, such as different sorting techniques in a program.

- **Adapter** pattern: You need to create different types of objects, but the exact type is determined at runtime.

- **Proxy** pattern: Controlling access to an object, such as caching or lazy initialization.

- **Factory** pattern: You want to simplify a complex subsystem by providing a unified interface.

- **Observer** pattern: Notifying multiple components when a particular event occurs, like in event-driven systems.

### Git Commands

- **Init**: Initializes a new Git repository
- **Checkout**: Downloads changes from a remote repository and merges them
- **Commit**: Saves staged changes. "Seal the envelope"
- **Add**: Stages changes, start tracking files. "Put them in the envelope"
- **Push**: Uploads local commits to a remote repository
- **Pull**: Applies any commits of the current branch ahead of specified one. Rewrites history
- **Rebase**: Initializes a new Git repository
- **Log**: Shows the commit history


### Code Review Benefits

- Showing your code to other people will:
  - **Help you find your defects**
  - Be a software review of your code
  - NOT be considered cheating in the academic world

### Software Complexity

- The amount of functionality, components, interfaces, and so on of the software refers to the **breadth** of software complexity.
- CI/CD stands for **Continuous Integration/Continuous Deployment**
- The term software engineering was first introduced in the year **1968** at the NATO conference in Germany to mimic the existing, traditional engineering disciplines.
- Frequent communication, simplicity in design and code, and feedback are three core values of **DevOps** programming.
- Main disadvantage of the Spiral Process model is **Low Complexity Management**

### Software Engineering Practices

- While Continuous Integration has been practiced since the 1970s, Continuous Integration and Continuous Deployment is a more recent practice. (**True**)
- The numbers of failures in software projects and defects encountered in the software products are **NOT** very few. (The statement "The numbers of failures in software projects and defects encountered in the software products are very few" is **False**)
- Software engineering is a broad field that touches upon all aspects of developing and supporting a software system. (**True**)
- Agile methods prefer **adapting to the people** over rigid processes. (The statement "Agile methods prefer rigid processes over adapting to the people" is **False**)
- There is **NOT** only one software engineering process model that fits each software project. (The statement "There is only one software engineering process model that fits each software project" is **False**)
- DevOps does **NOT** extend CI/CD to include IT Operations and Support. (The statement "DevOps extends CI/CD to include IT Operations and Support" is **False**)

### Technical Issues in Software Development

- Technical concerns in developing large systems can involve:
  - **The network**
  - Other concerns include: the database, version and configuration control

### Software Engineering Techniques

- A technique to "lessen" the relationships, number of functionalities, amount of interactions, and so on is **Integration** (although this may be incorrect - typically decomposition and modularization are used)

### Project Failure Reasons

- The main reasons projects were canceled, as uncovered by the Chaos report, are:
  - **Lack of resources and proper planning**

### Agile Processes

- Disadvantages of Agile processes include:
  - **Low process complexity**
- Advantages of agile processes include:
  - **Efficient handling of changes**
- Extreme programming practices writing test cases **before** writing the code.

### Software Architecture

- A system can be decomposed into different main modules. Each main module can be decomposed into smaller submodules. This decomposition can continue until the submodule is simple to design. (**True**)
- Service-Oriented Architecture (SOA) is an architectural style in which the architecture is divided into independent services, which are accessed only through the network. (**True**)
- Pre-condition is a condition that should be true if your module worked. (**False** - it should be true before the module executes)
- Programming libraries are not designed for reuse. (**False** - they are specifically designed for reuse)
- The CUPID principles completely replace SOLID, making SOLID principles obsolete in modern software development. (**False** - CUPID complements rather than replaces SOLID)
- In MVC, the Model is aware of the View and can directly communicate with it. (**True** - although traditional MVC often has the View observe the Model, not vice versa)

### REST Architecture

- The REST architecture is a:
  - **Style or pattern**

### Software Process Models

- **Waterfall**: A linear and sequential approach where each phase must be completed before moving to the next. (**E**)
- **Spiral**: A risk-driven model that combines iterative development with elements of prototyping. (**A**)
- **Incremental**: A method that builds the system in small parts, each adding functionality until completion. (**F**)
- **Scrum**: A framework that emphasizes teamwork, sprints, and iterative development with daily stand-ups. (**C**)
- **Agile**: A flexible and iterative approach that prioritizes customer collaboration and adaptability. (**D**)
- **XP**: A methodology that focuses on continuous feedback, pair programming, and test-driven development. (**B**)
- **DevOps**: A culture and practice that integrates development and operations for continuous delivery and automation. (**G**)

## Expected Exam Questions

1. **What is the difference between tasks and requirements in software engineering?**
   - Tasks define what a program needs to do, while requirements constrain how it can be designed and implemented.

2. **Explain the concept of black box testing and its importance.**
   - Black box testing focuses on testing based on requirements specifications without knowledge of the internal code, ensuring the software meets user requirements.

3. **What are the main advantages and disadvantages of the Agile development methodology?**
   - Advantages: Efficient handling of changes, customer collaboration, adaptability
   - Disadvantages: Low process complexity, may lack documentation, not ideal for all project types

4. **Compare and contrast Waterfall and Spiral process models.**
   - Waterfall is linear and sequential, while Spiral is risk-driven and combines iterative development with prototyping elements.

5. **What is the significance of CI/CD in modern software development?**
   - CI/CD (Continuous Integration/Continuous Deployment) automates the building, testing, and deployment process, leading to faster delivery and higher quality software.

6. **How does DevOps differ from traditional development approaches?**
   - DevOps integrates development and operations teams, focusing on automation, continuous delivery, and collaboration throughout the software lifecycle.

7. **Explain the concept of SOLID principles and their importance in software design.**
   - SOLID (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) provides guidelines for creating maintainable and scalable software systems.

8. **What is the purpose of software architecture patterns like MVC and REST?**
   - Architecture patterns provide proven solutions to common design problems, separating concerns and improving maintainability.

9. **Why is code review important in the software development process?**
   - Code reviews help find defects, share knowledge, ensure code quality, and maintain coding standards across the team.

10. **What are the main factors that contribute to software project failures?**
    - Lack of resources and proper planning, incomplete requirements, lack of user involvement, and poor communication are common factors.

11. **How do you estimate the time required for a software development task?**
    - Time estimation involves breaking down tasks, considering complexity, using historical data, and consulting with the development team.

12. **What is the role of testing in software development, and what are different types of testing?**
    - Testing verifies software quality and includes unit testing, integration testing, system testing, and acceptance testing.

13. **Explain the difference between architectural design and detailed design.**
    - Architectural design establishes the high-level structure and components of a system, while detailed design specifies the internal logic and algorithms.

14. **What is the Open/Closed Principle and why is it important?**
    - The Open/Closed Principle states that classes should be open for extension but closed for modification, promoting code stability and reusability.

15. **Describe the difference between concurrency and parallelism.**
    - Concurrency is about dealing with many things at once (structuring code to handle multiple tasks), while parallelism is about doing many things at once (executing multiple tasks simultaneously).

16. **What are design patterns and why are they important in software development?**
    - Design patterns are reusable solutions to common problems in software design. They're important because they provide tested, proven development paradigms that can speed up development and improve code quality.

17. **Explain the Liskov Substitution Principle and give an example.**
    - The Liskov Substitution Principle states that a subclass must be substitutable for its parent class without altering the correctness of the program. For example, if a program works with a "Bird" class, a "Penguin" subclass should work in the same contexts without requiring changes to the program, even though penguins can't fly.

18. **What are the best practices for logging in software applications?**
    - Best practices include: avoiding sensitive information (passwords), using structured formats (JSON), implementing appropriate log levels, including context, and ensuring logs are searchable and analyzable.

19. **Describe the git workflow and explain the purpose of key git commands.**
    - A typical git workflow involves initializing a repository (git init), making changes, staging them (git add), committing them (git commit), and pushing to a remote repository (git push). Commands like pull, checkout, and merge facilitate collaboration with other developers.

20. **What is the role of a Scrum Master versus a Tech Lead in an agile development team?**
    - A Scrum Master ensures that testing is properly integrated into the development process and facilitates the Scrum process, while a Tech Lead is responsible for setting coding standards and guiding technical decisions.

## Note for Exam Preparation

Focus on understanding the concepts rather than memorizing definitions. Pay special attention to:
- Software process models and their characteristics
- Agile methodologies and principles
- Testing approaches and their importance
- Factors affecting software quality and project success
- Modern development practices (CI/CD, DevOps)
- Software architecture concepts and patterns

Remember to review all quiz materials thoroughly and practice explaining concepts in your own words.
---


---


#


# CSC430 Software Engineering Study Guide

## Comprehensive Study Notes

### 1. Software Engineering Fundamentals

**Beyond the Quiz Material:**
- **Software Engineering Definition**: The application of systematic, disciplined, and quantifiable approaches to the development, operation, and maintenance of software.
- **Software Crisis Context**: The term "software engineering" emerged from the 1968 NATO conference in response to what was called the "software crisis" - projects running over budget, behind schedule, and with poor quality.
- **Key Differences from Programming**: Software engineering encompasses the entire software development lifecycle, while programming is just one phase. Software engineering also incorporates project management, requirements engineering, design, quality assurance, and maintenance.
- **Economic Importance**: Software failures can have enormous economic impacts - studies estimate software bugs cost the US economy about $59.5 billion annually.
- **Ethics in Software Engineering**: Professional codes of conduct (like the ACM Code of Ethics) guide software engineers in making ethical decisions about privacy, security, and social impact.

### 2. Software Development Processes

**Beyond the Quiz Material:**
- **Process Models Evolution**: Development processes have evolved from rigid plan-driven approaches to more flexible, iterative methods in response to increasing business volatility and technological change.
- **Waterfall Model Strengths**: Despite criticism, Waterfall remains appropriate for projects with stable requirements, well-understood technology, and regulatory constraints (like medical devices or avionics).
- **Agile Manifesto Principles**: The four values from the Agile Manifesto (2001): 1) Individuals and interactions over processes and tools; 2) Working software over comprehensive documentation; 3) Customer collaboration over contract negotiation; 4) Responding to change over following a plan.
- **Scaled Agile Frameworks**: For large organizations, frameworks like SAFe (Scaled Agile Framework), LeSS (Large-Scale Scrum), and Nexus have emerged to apply agile principles at enterprise scale.
- **Hybrid Approaches**: Many organizations use "hybrid" processes that combine elements of plan-driven and agile approaches, like "Water-Scrum-Fall" where planning is traditional, development is agile, and deployment follows a more controlled approach.
- **Organizational Culture Impact**: Process effectiveness is heavily influenced by organizational culture - the same process can succeed or fail based on cultural alignment.

### 3. Requirements Engineering

**Beyond the Quiz Material:**
- **Requirements Types Hierarchy**:
  - **Business Requirements**: The high-level needs of the organization or customer
  - **User Requirements**: Goals or tasks users must be able to perform
  - **Functional Requirements**: Software functionality
  - **Non-functional Requirements**: Quality attributes like performance, security, usability
  - **Implementation Requirements**: Technical constraints or standards
- **Requirements Elicitation Techniques**: Interviewing, workshops, observation, questionnaires, document analysis, and prototyping each have specific strengths and limitations.
- **User Stories Format**: The common "As a [role], I want [capability] so that [benefit]" format connects features to value.
- **Requirements Prioritization Methods**: MoSCoW (Must have, Should have, Could have, Won't have), Kano model (Basic, Performance, Excitement features), and Value vs. Cost mapping.
- **Requirements Traceability**: Maintaining bidirectional traceability between requirements and their sources, design elements, code, and tests is essential for impact analysis and verification.
- **Requirements Management Tools**: JIRA, Azure DevOps, and specialized tools like Doors provide support for managing requirements throughout the development lifecycle.

### 4. Software Architecture and Design

**Beyond the Quiz Material:**
- **Architectural Tactics**: Specific design decisions that influence quality attributes:
  - Performance tactics: caching, parallel processing, resource pooling
  - Security tactics: authentication, authorization, encryption, auditing
  - Availability tactics: fault detection, recovery, prevention
- **Architecture Evaluation Methods**: ATAM (Architecture Tradeoff Analysis Method) and SAAM (Software Architecture Analysis Method) provide structured approaches to evaluating architectures.
- **Conway's Law**: "Organizations design systems that mirror their communication structure." Understanding this relationship helps align team structure with desired architecture.
- **Technical Debt**: Architectural and design decisions that save time in the short term but create extra work later. Types include deliberate (strategic shortcuts) and inadvertent (lack of knowledge).
- **Architecture Documentation**: Views and beyond approach (Kruchten's 4+1 view model) documents architecture from multiple perspectives: logical, development, process, and physical views, plus scenarios.
- **Domain-Driven Design**: An approach that focuses on the core domain and domain logic, placing emphasis on the domain model rather than technical aspects.
- **Architectural Patterns Beyond MVC**:
  - Microkernel: Core system and plug-in modules (IDEs, browsers)
  - Event-driven: Components communicate through events (GUIs, IoT)
  - Layered: Hierarchical organization (network protocols)
  - Pipes and filters: Data transformation pipeline (compilers, data processing)
  - Space-based: High scalability through shared tuple space (trading systems)

### 5. Design Patterns in Detail

**Beyond the Quiz Material:**
- **Pattern Categories**:
  - **Creational**: Abstract Factory, Builder, Factory Method, Prototype, Singleton
  - **Structural**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
  - **Behavioral**: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor
- **Anti-patterns**: Recognized solutions that generate more problems:
  - **God Class/Blob**: A class that does or knows too much
  - **Spaghetti Code**: Unstructured and difficult-to-maintain code
  - **Golden Hammer**: Trying to solve every problem with the same tool
  - **Dead Code**: Unused code that clutters the codebase
  - **Lava Flow**: Dead code that can't be easily removed due to dependencies
- **Pattern Context**: Patterns should be applied based on context, not dogmatically. Each pattern comes with tradeoffs.
- **Composite Patterns**: Patterns often work together - e.g., Factory Method often creates objects for a Strategy pattern.
- **Refactoring to Patterns**: Gradually evolving code toward pattern implementations rather than forcing them initially.

### 6. Software Testing and Quality Assurance

**Beyond the Quiz Material:**
- **Testing Quadrants**: Brian Marick's model categorizes tests as:
  - Business-facing tests that support the team (functional acceptance tests)
  - Business-facing tests that critique the product (exploratory testing, usability)
  - Technology-facing tests that support the team (unit tests, component tests)
  - Technology-facing tests that critique the product (performance, security)
- **Test-Driven Development (TDD) Cycle**: Red (write a failing test), Green (make it pass with minimal code), Refactor (improve the implementation without changing behavior).
- **Behavior-Driven Development (BDD)**: Extends TDD with a focus on business behavior using a ubiquitous language (Given-When-Then format).
- **Testing Pyramid**: Proportional distribution of tests: many unit tests, fewer integration tests, even fewer UI/end-to-end tests.
- **Mutation Testing**: Automatically introducing defects to evaluate test effectiveness.
- **Property-Based Testing**: Generating random inputs to verify properties that should hold true.
- **Quality Models**: Frameworks like ISO/IEC 25010 define quality characteristics (functionality, reliability, usability, efficiency, maintainability, portability).
- **Quality Attributes Tradeoffs**: Enhancing certain qualities often diminishes others (e.g., adding security features may reduce performance).
- **Continuous Testing**: Integration of testing throughout the development pipeline rather than as a separate phase.

### 7. Version Control and Collaboration

**Beyond the Quiz Material:**
- **Distributed vs. Centralized VCS**: Git/Mercurial (distributed) vs. SVN/CVS (centralized) - tradeoffs in workflow flexibility, learning curve, and performance.
- **Branching Strategies**:
  - **Gitflow**: Long-lived development and main branches with feature, release, and hotfix branches
  - **GitHub Flow**: Feature branches from main with frequent integration
  - **Trunk-based Development**: Working primarily on the main branch with feature toggles
  - **Release Train**: Time-boxed releases from development branch
- **Git Internals**: Understanding Git's object model (blobs, trees, commits) and reference system helps resolve complex issues.
- **Advanced Git Operations**: Interactive rebase, cherry-pick, bisect, reflog, and submodules for advanced workflow needs.
- **Code Review Best Practices**: Small, focused changes; clear descriptions; automated checks before human review; balanced feedback focused on the code, not the author.
- **Code Ownership Models**: Strong (individuals own files), Weak (team consensus required for changes), Collective (anyone can change anything).
- **Pull Request Workflow**: Fork-and-pull vs. shared repository models; integrating automated tests, code quality checks, and security scanning.

### 8. DevOps and Continuous Integration/Delivery

**Beyond the Quiz Material:**
- **DevOps Cultural Principles**: Culture of collaboration, focus on customer value, embracing failure as learning, continuous improvement.
- **Continuous Integration Components**: Source control integration, automated builds, test automation, deployment automation, environment management.
- **Deployment Strategies**:
  - **Blue-Green**: Maintaining two identical environments for zero-downtime switching
  - **Canary**: Gradual rollout to a subset of users
  - **Feature Toggles**: Deploying inactive code that can be enabled without redeployment
  - **A/B Testing**: Testing different versions simultaneously
- **Infrastructure as Code (IaC)**: Managing infrastructure through code (Terraform, CloudFormation, Ansible) for consistency and version control.
- **Containerization and Orchestration**: Docker containers and orchestration tools like Kubernetes provide consistent environments and scaling.
- **Monitoring and Observability**: Metrics, logging, tracing, and alerting form a comprehensive observability strategy.
- **CI/CD Security**: Integrating security scanning (SAST, DAST, SCA) into the pipeline; securing the pipeline itself from tampering.
- **Value Stream Mapping**: Analyzing the steps from concept to customer to eliminate waste and improve flow.

### 9. Software Project Management

**Beyond the Quiz Material:**
- **Project Constraints**: The triple constraint (scope, schedule, resources) plus quality - changes to one affect the others.
- **Estimation Techniques**:
  - **Expert Judgment**: Leveraging team experience
  - **Analogous Estimation**: Based on similar past projects
  - **Parametric Estimation**: Mathematical models based on characteristics
  - **Three-Point Estimation**: (Optimistic + 4 × Most Likely + Pessimistic) ÷ 6
  - **Planning Poker**: Collaborative consensus-building
  - **Story Points**: Relative sizing based on complexity, effort, and uncertainty
- **Risk Management Process**: Identification, analysis, prioritization, response planning, monitoring.
- **Earned Value Management**: Tracking project performance through metrics like CPI (Cost Performance Index) and SPI (Schedule Performance Index).
- **Team Performance Models**: Tuckman's stages (Forming, Storming, Norming, Performing, Adjourning); Lencioni's Five Dysfunctions.
- **Technical Debt Management**: Strategies for identifying, measuring, prioritizing, and addressing technical debt.
- **Project Portfolio Management**: Balancing resources across multiple projects; aligning projects with strategic objectives.

### 10. Software Maintenance and Evolution

**Beyond the Quiz Material:**
- **Maintenance Categories**:
  - **Corrective**: Fixing defects
  - **Adaptive**: Adapting to changing environment
  - **Perfective**: Enhancing functionality
  - **Preventive**: Improving future maintainability
- **Legacy System Strategies**: Replacement, reengineering, migration, encapsulation, and incremental modernization.
- **Software Aging Factors**: Technology changes, business changes, staff turnover, and knowledge loss.
- **Refactoring Techniques**: Extract method/class, rename, move method/field, replace conditional with polymorphism, etc.
- **Code Smells**: Indicators of potential problems (duplicated code, long methods, large classes, feature envy, etc.).
- **Reverse Engineering**: Techniques for understanding undocumented systems (static analysis, dynamic analysis, feature location).
- **Configuration Management**: Managing changes to requirements, design, code, and documentation throughout the system lifecycle.
- **Software Metrics for Maintenance**: Measuring maintainability through complexity, coupling, cohesion, and change impact metrics.

### 11. Software Ethics and Professional Practice

**Beyond the Quiz Material:**
- **Software Engineering Code of Ethics**: Principles from the ACM/IEEE-CS:
  - Public interest as paramount concern
  - Client and employer interests
  - Product quality and professional judgment
  - Integrity and independence
  - Professional development and ethical management
  - Profession advancement and collegiality
- **Intellectual Property in Software**: Understanding copyright, patents, trade secrets, and licensing (proprietary, open-source, copyleft).
- **Privacy by Design**: Integrating privacy protection throughout the development process rather than adding it later.
- **Accessibility Standards**: WCAG guidelines for making software accessible to people with disabilities.
- **Ethics of AI and Automation**: Addressing bias, fairness, transparency, and accountability in automated systems.
- **Whistleblowing**: Professional responsibility in reporting unethical practices and legal protections.
- **Sustainability**: Environmental impact of software through energy consumption and hardware obsolescence.
- **Cultural and Global Issues**: Developing software for diverse global audiences; addressing cultural differences in teams.

## Key Concepts from Quizzes (Spring 2025)

### Software Design & Architecture

- Designing how to represent the data required for the software system and how to store it efficiently is part of **all of these**: Detail design, Database design, and Requirement design.

- The difference between Service-Oriented and Microservices architectures is:
  - **SOA does not support reusability, while Microservices are designed for maximum code reuse**
  - (Note: Other differences include: Microservices are typically smaller in scope/size, and Microservices typically use an Enterprise Service Bus while SOA services communicate directly)

- The primary difference between architectural design and detailed design in software engineering:
  - **Architectural design establishes the high-level structure and components of a system, while detailed design specifies the internal logic and algorithms**

- The Open/Closed Principle (OCP) states:
  - **Classes should be open for extension but closed for modification**
  - (Not "A class should always be publicly accessible" or "A class should never be extended or modified")

- For best design we want to achieve strong cohesion and tight coupling, with strong cohesion referring to how well-focused a module's responsibilities are, and tight coupling referring to how independent modules are from each other.

### Basic Terminology

- **Tasks** are statements that define or qualify what a program needs to do.
- **Requirements** are statements that constrain the ways in which the software can be designed and implemented.
- **Lack of Communication** is one of the two major examples of growth in depth of complexity.
- **User Interface** is an interface with graphical icons to communicate to users.
- The **Task** qualify the functional requirements and specify in what manner they need to be achieved.

### Agile and Development Roles

- When a software release is repeatedly failing in production due to untested features, the **Scrum Master** should ensure that testing is properly integrated into the development process.

- A development team struggling with poor code quality and frequent technical debt means the **Tech Lead** is primarily responsible for setting coding standards and guiding technical decisions.

### Code Quality & Testing

- What is the best type of comment to have in your code? **Explanation of the code**

- The four phases of debugging are: **Reproduction, Localization, Verification, Report**

- Boundary value analysis focuses on: **Examining values at the limit, just under, and just over**

- A software "build" is best described as: **A set of activities associated with the integration and conversion of source files to a set of executable files**

- Artifacts that are not related to each other: **User-interface screens and code segments**

- What is not a candidate for multithreading: **Usage of a Log file**

### Concurrency & Multithreading

- What is true about multithreaded environment: **Threads are always executed in parallel**

- The difference between concurrency and parallelism:
  - **Concurrency is about dealing with many things at once (structuring code to handle multiple tasks), while parallelism is about doing many things at once (executing multiple tasks simultaneously)**

- The primary purpose of using an API (Application Programming Interface) in a software application:
  - **To enable communication between different software systems or components by providing predefined functions and protocols**

### Software Quality & Testing

### Object Relationships

- The best kind of relationship the following objects should have: Bicycle/Wheels and Bicycle/Frame Parts? **Dependency and Realization**

### Design Patterns

- **Singleton** pattern: Ensuring that only one instance of a class exists in an application, such as a configuration manager.

- **Facade** pattern: Converting an interface of one class into another that a client expects.

- **Builder** pattern: Constructing complex objects step by step, such as assembling a meal order in a restaurant system.

- **Strategy** pattern: Defining a family of interchangeable algorithms, such as different sorting techniques in a program.

- **Adapter** pattern: You need to create different types of objects, but the exact type is determined at runtime.

- **Proxy** pattern: Controlling access to an object, such as caching or lazy initialization.

- **Factory** pattern: You want to simplify a complex subsystem by providing a unified interface.

- **Observer** pattern: Notifying multiple components when a particular event occurs, like in event-driven systems.

### Git Commands

- **Init**: Initializes a new Git repository
- **Checkout**: Downloads changes from a remote repository and merges them
- **Commit**: Saves staged changes. "Seal the envelope"
- **Add**: Stages changes, start tracking files. "Put them in the envelope"
- **Push**: Uploads local commits to a remote repository
- **Pull**: Applies any commits of the current branch ahead of specified one. Rewrites history
- **Rebase**: Initializes a new Git repository
- **Log**: Shows the commit history


### Code Review Benefits

- Showing your code to other people will:
  - **Help you find your defects**
  - Be a software review of your code
  - NOT be considered cheating in the academic world

### Software Complexity

- The amount of functionality, components, interfaces, and so on of the software refers to the **breadth** of software complexity.
- CI/CD stands for **Continuous Integration/Continuous Deployment**
- The term software engineering was first introduced in the year **1968** at the NATO conference in Germany to mimic the existing, traditional engineering disciplines.
- Frequent communication, simplicity in design and code, and feedback are three core values of **DevOps** programming.
- Main disadvantage of the Spiral Process model is **Low Complexity Management**

### Software Engineering Practices

- While Continuous Integration has been practiced since the 1970s, Continuous Integration and Continuous Deployment is a more recent practice. (**True**)
- The numbers of failures in software projects and defects encountered in the software products are **NOT** very few. (The statement "The numbers of failures in software projects and defects encountered in the software products are very few" is **False**)
- Software engineering is a broad field that touches upon all aspects of developing and supporting a software system. (**True**)
- Agile methods prefer **adapting to the people** over rigid processes. (The statement "Agile methods prefer rigid processes over adapting to the people" is **False**)
- There is **NOT** only one software engineering process model that fits each software project. (The statement "There is only one software engineering process model that fits each software project" is **False**)
- DevOps does **NOT** extend CI/CD to include IT Operations and Support. (The statement "DevOps extends CI/CD to include IT Operations and Support" is **False**)

### Technical Issues in Software Development

- Technical concerns in developing large systems can involve:
  - **The network**
  - Other concerns include: the database, version and configuration control

### Software Engineering Techniques

- A technique to "lessen" the relationships, number of functionalities, amount of interactions, and so on is **Integration** (although this may be incorrect - typically decomposition and modularization are used)

### Project Failure Reasons

- The main reasons projects were canceled, as uncovered by the Chaos report, are:
  - **Lack of resources and proper planning**

### Agile Processes

- Disadvantages of Agile processes include:
  - **Low process complexity**
- Advantages of agile processes include:
  - **Efficient handling of changes**
- Extreme programming practices writing test cases **before** writing the code.

### Software Architecture

- A system can be decomposed into different main modules. Each main module can be decomposed into smaller submodules. This decomposition can continue until the submodule is simple to design. (**True**)
- Service-Oriented Architecture (SOA) is an architectural style in which the architecture is divided into independent services, which are accessed only through the network. (**True**)
- Pre-condition is a condition that should be true if your module worked. (**False** - it should be true before the module executes)
- Programming libraries are not designed for reuse. (**False** - they are specifically designed for reuse)
- The CUPID principles completely replace SOLID, making SOLID principles obsolete in modern software development. (**False** - CUPID complements rather than replaces SOLID)
- In MVC, the Model is aware of the View and can directly communicate with it. (**True** - although traditional MVC often has the View observe the Model, not vice versa)

### REST Architecture

- The REST architecture is a:
  - **Style or pattern**

### Software Process Models

- **Waterfall**: A linear and sequential approach where each phase must be completed before moving to the next. (**E**)
- **Spiral**: A risk-driven model that combines iterative development with elements of prototyping. (**A**)
- **Incremental**: A method that builds the system in small parts, each adding functionality until completion. (**F**)
- **Scrum**: A framework that emphasizes teamwork, sprints, and iterative development with daily stand-ups. (**C**)
- **Agile**: A flexible and iterative approach that prioritizes customer collaboration and adaptability. (**D**)
- **XP**: A methodology that focuses on continuous feedback, pair programming, and test-driven development. (**B**)
- **DevOps**: A culture and practice that integrates development and operations for continuous delivery and automation. (**G**)

## Expected Exam Questions

1. **What is the difference between tasks and requirements in software engineering?**
   - Tasks define what a program needs to do, while requirements constrain how it can be designed and implemented.

2. **Explain the concept of black box testing and its importance.**
   - Black box testing focuses on testing based on requirements specifications without knowledge of the internal code, ensuring the software meets user requirements.

3. **What are the main advantages and disadvantages of the Agile development methodology?**
   - Advantages: Efficient handling of changes, customer collaboration, adaptability
   - Disadvantages: Low process complexity, may lack documentation, not ideal for all project types

4. **Compare and contrast Waterfall and Spiral process models.**
   - Waterfall is linear and sequential, while Spiral is risk-driven and combines iterative development with prototyping elements.

5. **What is the significance of CI/CD in modern software development?**
   - CI/CD (Continuous Integration/Continuous Deployment) automates the building, testing, and deployment process, leading to faster delivery and higher quality software.

6. **How does DevOps differ from traditional development approaches?**
   - DevOps integrates development and operations teams, focusing on automation, continuous delivery, and collaboration throughout the software lifecycle.

7. **Explain the concept of SOLID principles and their importance in software design.**
   - SOLID (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) provides guidelines for creating maintainable and scalable software systems.

8. **What is the purpose of software architecture patterns like MVC and REST?**
   - Architecture patterns provide proven solutions to common design problems, separating concerns and improving maintainability.

9. **Why is code review important in the software development process?**
   - Code reviews help find defects, share knowledge, ensure code quality, and maintain coding standards across the team.

10. **What are the main factors that contribute to software project failures?**
    - Lack of resources and proper planning, incomplete requirements, lack of user involvement, and poor communication are common factors.

11. **How do you estimate the time required for a software development task?**
    - Time estimation involves breaking down tasks, considering complexity, using historical data, and consulting with the development team.

12. **What is the role of testing in software development, and what are different types of testing?**
    - Testing verifies software quality and includes unit testing, integration testing, system testing, and acceptance testing.

13. **Explain the difference between architectural design and detailed design.**
    - Architectural design establishes the high-level structure and components of a system, while detailed design specifies the internal logic and algorithms.

14. **What is the Open/Closed Principle and why is it important?**
    - The Open/Closed Principle states that classes should be open for extension but closed for modification, promoting code stability and reusability.

15. **Describe the difference between concurrency and parallelism.**
    - Concurrency is about dealing with many things at once (structuring code to handle multiple tasks), while parallelism is about doing many things at once (executing multiple tasks simultaneously).

16. **What are design patterns and why are they important in software development?**
    - Design patterns are reusable solutions to common problems in software design. They're important because they provide tested, proven development paradigms that can speed up development and improve code quality.

17. **Explain the Liskov Substitution Principle and give an example.**
    - The Liskov Substitution Principle states that a subclass must be substitutable for its parent class without altering the correctness of the program. For example, if a program works with a "Bird" class, a "Penguin" subclass should work in the same contexts without requiring changes to the program, even though penguins can't fly.

18. **What are the best practices for logging in software applications?**
    - Best practices include: avoiding sensitive information (passwords), using structured formats (JSON), implementing appropriate log levels, including context, and ensuring logs are searchable and analyzable.

19. **Describe the git workflow and explain the purpose of key git commands.**
    - A typical git workflow involves initializing a repository (git init), making changes, staging them (git add), committing them (git commit), and pushing to a remote repository (git push). Commands like pull, checkout, and merge facilitate collaboration with other developers.

20. **What is the role of a Scrum Master versus a Tech Lead in an agile development team?**
    - A Scrum Master ensures that testing is properly integrated into the development process and facilitates the Scrum process, while a Tech Lead is responsible for setting coding standards and guiding technical decisions.

## Note for Exam Preparation

Focus on understanding the concepts rather than memorizing definitions. Pay special attention to:
- Software process models and their characteristics
- Agile methodologies and principles
- Testing approaches and their importance
- Factors affecting software quality and project success
- Modern development practices (CI/CD, DevOps)
- Software architecture concepts and patterns

Remember to review all quiz materials thoroughly and practice explaining concepts in your own words.


# SIMPLE NOTES:

---
`I most read this...`
## Software Testing Concepts

### Testing Types

1. **Black Box Testing**
   - Tests the functionality of an application without knowledge of its internal code structure
   - Based solely on requirements specifications
   - Only examines inputs and outputs, not how the software works internally
   - Also called functional or behavioral testing
   - Examples: acceptance testing, system testing

2. **White Box Testing**
   - Tests the internal structure and working of the application
   - Requires knowledge of the code implementation
   - Tests paths, conditions, loops, and statements in the code
   - Also called structural or glass box testing
   - Examples: unit testing, code coverage analysis

3. **Gray Box Testing**
   - Combines elements of both black box and white box testing
   - Testers have partial knowledge of the internal workings
   - Common in integration testing and penetration testing

### Testing Levels

1. **Unit Testing**
   - Tests individual units or components of code in isolation
   - Usually performed by developers
   - Verifies that each unit of code works as expected
   - Often automated with frameworks like JUnit, NUnit, or pytest

2. **Integration Testing**
   - Tests combinations of units to verify they work together correctly
   - Approaches include:
     - **Big Bang Integration**: All components are integrated simultaneously
     - **Incremental Integration**: Components are integrated one at a time
     - **Top-Down Integration**: Testing from higher-level modules to lower modules
     - **Bottom-Up Integration**: Testing from lower-level modules to higher modules

3. **System Testing**
   - Tests the complete, integrated software system
   - Verifies that the system meets its requirements
   - Performed in an environment similar to production
   - Tests functionality, performance, security, etc.

4. **Acceptance Testing**
   - Verifies that the system satisfies business requirements
   - Determines if the system is ready for delivery
   - Types include:
     - **User Acceptance Testing (UAT)**: Performed by end users
     - **Alpha Testing**: Performed by internal teams in a simulated environment
     - **Beta Testing**: Performed by a limited number of real users

### Testing Approaches

1. **Manual Testing**
   - Tests executed by a human tester
   - Exploratory testing, usability testing often performed manually
   - More flexible but time-consuming and prone to human error

2. **Automated Testing**
   - Tests executed by software tools
   - More efficient for repetitive tests and regression testing
   - Requires initial investment in creating test scripts
   - Tools include Selenium, JUnit, TestNG, Cypress

3. **Static Testing**
   - Examines software artifacts without executing code
   - Includes code reviews, inspections, walkthroughs
   - Can identify defects early in development

4. **Dynamic Testing**
   - Involves executing the code and analyzing behavior
   - Examines how the software behaves during runtime
   - Most common form of testing

### Specialized Testing Types

1. **Regression Testing**
   - Re-running tests to ensure that previously working functionality still works after changes
   - Critical for maintaining software quality during updates
   - Often automated to reduce effort

2. **Performance Testing**
   - Evaluates how the system performs under specific conditions
   - Subtypes include:
     - **Load Testing**: System behavior under expected load
     - **Stress Testing**: System behavior under extreme load
     - **Endurance Testing**: System behavior over extended periods
     - **Spike Testing**: System response to sudden increases in load

3. **Security Testing**
   - Identifies vulnerabilities in the software
   - Includes penetration testing, vulnerability scanning
   - Verifies protection of data and functionality

4. **Usability Testing**
   - Evaluates how easy the software is to use
   - Often involves real users performing specific tasks
   - Measures efficiency, effectiveness, and satisfaction

5. **Compatibility Testing**
   - Checks if software works across different environments
   - Tests compatibility with various hardware, operating systems, browsers, network environments

6. **Exploratory Testing**
   - Simultaneous learning, test design, and test execution
   - Less structured, relies on tester's creativity and knowledge
   - Useful for finding defects missed by scripted tests

### Test Design Techniques

1. **Equivalence Partitioning**
   - Divides input data into equivalent classes
   - Tests representative values from each class
   - Reduces number of test cases needed

2. **Boundary Value Analysis**
   - Tests values at the boundaries of equivalence classes
   - Examines values at the limit, just under, and just over
   - Effective because defects often occur at boundaries

3. **Decision Table Testing**
   - Uses tables to represent combinations of inputs and their corresponding outputs
   - Effective for complex business logic with multiple conditions

4. **State Transition Testing**
   - Models system as a finite state machine
   - Tests transitions between states
   - Useful for systems with different operational modes

5. **Use Case Testing**
   - Tests end-to-end scenarios from user perspective
   - Based on use cases that describe user interactions

### Test Documentation

1. **Test Plan**
   - Comprehensive document outlining testing approach, objectives, scope, schedule, and resources
   - Defines what will be tested and how

2. **Test Case**
   - Specific set of test inputs, execution conditions, and expected results
   - Documents steps to verify specific functionality

3. **Test Scenario**
   - High-level description of functionality to be tested
   - Usually contains multiple test cases

4. **Test Script**
   - Detailed instructions for test execution
   - May be written for manual execution or automated testing

5. **Defect Report (Bug Report)**
   - Documents issues found during testing
   - Typically includes severity, priority, steps to reproduce, expected vs. actual results

### Testing Principles

1. **Early Testing**
   - Testing should start as early as possible in the development lifecycle
   - Finding defects early reduces cost of fixing them

2. **Exhaustive Testing is Impossible**
   - Cannot test all input combinations and scenarios
   - Need to prioritize testing based on risk and importance

3. **Defect Clustering**
   - Defects tend to cluster in certain modules or functionality
   - 80% of defects often found in 20% of modules

4. **Pesticide Paradox**
   - Repeatedly running the same tests will eventually stop finding new bugs
   - Test cases need to be regularly reviewed and updated

5. **Testing Shows Presence of Defects**
   - Testing can show defects exist but cannot prove their absence
   - Cannot prove software is 100% defect-free

6. **Context Dependent Testing**
   - Testing approach depends on the context of the software
   - Different applications require different testing approaches

7. **Absence of Errors Fallacy**
   - Finding and fixing defects doesn't help if the system doesn't meet user needs
   - Must verify system meets requirements and user expectations

### Test-Driven Development (TDD)

1. **TDD Process**
   - Write a failing test first (Red)
   - Write minimal code to pass the test (Green)
   - Refactor the code while keeping tests passing (Refactor)
   - Repeat for each feature

2. **Benefits of TDD**
   - Ensures code is testable by design
   - Provides immediate feedback on code quality
   - Creates a comprehensive test suite
   - Encourages simple designs and modular code

### Continuous Testing

1. **Integration with CI/CD**
   - Tests automatically run when code changes are committed
   - Provides immediate feedback to developers
   - Prevents integration of defective code

2. **Test Environments**
   - Development: Initial testing during development
   - Integration: Testing integrated components
   - Staging: Testing in production-like environment
   - Production: Monitoring and testing in live environment

### Testing Metrics

1. **Test Coverage**
   - Measures how much of the code is exercised by tests
   - Types include:
     - **Statement Coverage**: Percentage of statements executed
     - **Branch Coverage**: Percentage of branches (decisions) executed
     - **Path Coverage**: Percentage of possible paths executed

2. **Defect Metrics**
   - Defect density (defects per KLOC)
   - Defect detection percentage
   - Defect leakage (defects that escape to later phases)

3. **Test Execution Metrics**
   - Test pass rate
   - Test execution time
   - Number of automated vs. manual tests

# MORE STUDY NOTES:


---

\n

`Small Note`


# Software Architecture Concepts

## Fundamental Concepts

1. **Definition and Purpose**
   - A high-level structure of a software system, components, and their interactions
   - Acts as a blueprint guiding development, maintenance, and evolution
   - Balances functionality with quality attributes (performance, security, maintainability)
   - Addresses both technical and business concerns

2. **Architecture vs. Design**
   - **Architectural Design**: Establishes the high-level structure and components of a system, focusing on the "big picture"
   - **Detailed Design**: Specifies the internal logic and algorithms within components identified by architecture
   - Architecture addresses system-wide decisions; design implements those decisions at component level
   - Architecture decisions are harder to change later than design decisions

3. **Architectural Significance**
   - Not all decisions are architecturally significant
   - Criteria for architectural significance:
     - Affects multiple components or stakeholders
     - Difficult or expensive to change later
     - Impacts critical quality attributes
     - Involves system-level concepts

## Architecture Quality Attributes

1. **Performance**
   - Response time, throughput, latency, resource utilization
   - Tactics: caching, load balancing, parallel processing, resource pooling, asynchronous processing

2. **Scalability**
   - Ability to handle growth in users, data, transactions
   - Horizontal scaling (adding more machines) vs. vertical scaling (more powerful machines)
   - Tactics: partitioning, replication, statelessness, asynchronous communication

3. **Reliability**
   - System operates correctly over time under specified conditions
   - Measured by mean time between failures (MTBF)
   - Tactics: fault detection, recovery, prevention, redundancy

4. **Availability**
   - System accessible and operational when needed
   - Often expressed as percentage of uptime (e.g., 99.9%)
   - Tactics: fault tolerance, redundancy, monitoring, failover mechanisms

5. **Security**
   - Protection against unauthorized access and attacks
   - Confidentiality, integrity, availability, non-repudiation
   - Tactics: authentication, authorization, encryption, input validation, auditing

6. **Maintainability**
   - Ease of modifying and enhancing the system
   - Measured by time/effort to implement changes
   - Tactics: modularity, information hiding, standardization, documentation

7. **Usability**
   - Ease of learning and using the system
   - Tactics: user feedback, consistent interface, help systems, error prevention

8. **Interoperability**
   - Ability to exchange information with other systems
   - Tactics: standard protocols, API definitions, middleware, data transformations

## Architectural Patterns

1. **Layered Architecture**
   - Organizes system into horizontal layers with specific responsibilities
   - Each layer provides services to the layer above and uses services from the layer below
   - Examples: OSI model, typical enterprise applications (presentation, business, data access)
   - Benefits: separation of concerns, module replaceability, clear dependencies
   - Drawbacks: performance overhead, unnecessary coupling through middle layers

2. **Client-Server**
   - Distributes functionality between service providers (servers) and service consumers (clients)
   - Server provides resources or functionality; clients request these services
   - Examples: web applications, database systems, email systems
   - Benefits: centralized control, scalability, clear separation
   - Drawbacks: server can become bottleneck, network dependency

3. **Model-View-Controller (MVC)**
   - Separates application into three logical components:
     - **Model**: Data and business logic
     - **View**: User interface elements
     - **Controller**: Handles user input and orchestrates model/view updates
   - Examples: web frameworks (Django, Rails, Spring MVC)
   - Benefits: separation of concerns, multiple views for same model, parallel development
   - Drawbacks: increased complexity for simple applications

4. **Pipe and Filter**
   - Processing elements (filters) connected by communication channels (pipes)
   - Each filter performs a specific transformation on input data and produces output
   - Examples: compilers, ETL processes, Unix command line
   - Benefits: reusability of filters, easy addition/reconfiguration, parallelism
   - Drawbacks: may not be suitable for interactive applications, potential data transformation overhead

5. **Microservices**
   - System composed of small, independent services that focus on specific business capabilities
   - Services communicate through lightweight protocols (HTTP/REST, messaging)
   - Each service has its own database and can be deployed independently
   - Benefits: independent development/deployment, technology diversity, resilience, scalability
   - Drawbacks: distributed system complexity, potential network overhead, service coordination challenges

6. **Service-Oriented Architecture (SOA)**
   - Organizes functionality as a collection of interoperable services
   - Services are self-contained, loosely coupled, and accessible through standard interfaces
   - Often includes an Enterprise Service Bus (ESB) for message routing and transformation
   - Benefits: service reuse, interoperability, adaptability to business changes
   - Drawbacks: complexity of service management, potential performance overhead, governance challenges

7. **Event-Driven Architecture**
   - Components communicate through events rather than direct calls
   - Publishers emit events without knowing consumers; subscribers react to events
   - Examples: UI systems, real-time analytics, IoT applications
   - Benefits: loose coupling, scalability, responsiveness, adaptability
   - Drawbacks: complex debugging, potential unpredictability, eventual consistency challenges

8. **Hexagonal/Ports and Adapters**
   - Core business logic at center, surrounded by ports (interfaces) and adapters
   - Separates business logic from external concerns (UI, database, services)
   - Benefits: testability, technology independence, focus on domain logic
   - Drawbacks: additional abstraction layers, potential overengineering for simple applications

## Architecture Styles

1. **Monolithic**
   - Single, unified codebase and deployment unit
   - All components tightly integrated and deployed together
   - Benefits: simplicity, easier testing, performance
   - Drawbacks: scalability limitations, technology lock-in, all-or-nothing deployment

2. **Distributed**
   - Components deployed across multiple physical or virtual machines
   - Communicate via network protocols (RPC, messaging, etc.)
   - Benefits: scalability, fault isolation, geographic distribution
   - Drawbacks: network latency, complexity, partial failures

3. **Cloud-Native**
   - Designed specifically for cloud deployment and scaling
   - Emphasizes containerization, automation, orchestration
   - Leverages managed services and cloud provider capabilities
   - Benefits: elasticity, resilience, cost optimization
   - Drawbacks: potential vendor lock-in, distributed system challenges

4. **Serverless**
   - Functions deployed individually, executed on-demand
   - Infrastructure managed by provider, scales automatically
   - Benefits: reduced operational complexity, pay-per-use, auto-scaling
   - Drawbacks: limited execution duration, cold start latency, debugging challenges

## Architectural Documentation

1. **Views and Viewpoints**
   - Different perspectives based on stakeholder concerns
   - Common views:
     - **Logical/Structural View**: Components and their relationships
     - **Development View**: Code organization, modules, dependencies
     - **Process View**: Runtime elements, communication, concurrency
     - **Physical View**: Deployment, hardware mapping
     - **Scenarios**: Use cases that illustrate architecture behavior

2. **Kruchten's 4+1 View Model**
   - Four views plus scenarios that tie them together
   - Logical, development, process, and physical views
   - Scenarios demonstrate how architecture supports key requirements

3. **Documentation Approaches**
   - Architecture Decision Records (ADRs): Document key decisions and rationales
   - UML diagrams: Component, deployment, sequence, class diagrams
   - C4 Model: Context, containers, components, and code
   - Arc42: Template-based documentation framework

## Architectural Analysis and Evaluation

1. **Architecture Tradeoff Analysis Method (ATAM)**
   - Evaluates architecture decisions against quality attribute requirements
   - Identifies sensitivity points, tradeoffs, and risks
   - Involves multiple stakeholders in structured analysis sessions

2. **Cost Benefit Analysis Method (CBAM)**
   - Extends ATAM with economic considerations
   - Quantifies costs and benefits of architectural decisions
   - Helps prioritize architectural strategies

3. **Active Reviews for Intermediate Designs (ARID)**
   - Lightweight review focused on a portion of the architecture
   - Evaluates if the design can support specific use cases
   - Identifies issues early in the design process

## Architecture Principles (SOLID for Architecture)

1. **Single Responsibility Principle (SRP)**
   - Each component should have only one reason to change
   - Maps to high cohesion at the architectural level

2. **Open/Closed Principle (OCP)**
   - Architecture should be open for extension but closed for modification
   - New functionality added without changing existing components

3. **Liskov Substitution Principle (LSP)**
   - Components should be substitutable for their abstractions
   - Interface consistency across implementations

4. **Interface Segregation Principle (ISP)**
   - Fine-grained interfaces specific to client needs
   - Avoid forcing clients to depend on interfaces they don't use

5. **Dependency Inversion Principle (DIP)**
   - High-level modules should not depend on low-level modules
   - Both should depend on abstractions
   - Abstractions should not depend on details

## Modern Architecture Concepts

1. **Domain-Driven Design (DDD)**
   - Aligns software architecture with business domain
   - Key concepts: bounded contexts, ubiquitous language, aggregates, entities, value objects
   - Strategic and tactical patterns for complex domain modeling

2. **Command Query Responsibility Segregation (CQRS)**
   - Separates read (query) operations from write (command) operations
   - Can use different models and even different databases for each
   - Benefits: scalability, performance, flexibility
   - Drawbacks: increased complexity, eventual consistency challenges

3. **Event Sourcing**
   - Stores changes to application state as a sequence of events
   - System state reconstructed by replaying events
   - Benefits: complete audit trail, temporal queries, performance for write-heavy systems
   - Drawbacks: query complexity, eventual consistency, learning curve

4. **Reactive Architecture**
   - Designed to be responsive, resilient, elastic, and message-driven
   - Emphasizes asynchronous communication and non-blocking operations
   - Based on Reactive Manifesto principles
   - Benefits: responsiveness under load, resilience to failures, scalability
   - Drawbacks: complexity, debugging challenges, paradigm shift

5. **Containerization and Orchestration**
   - Packaging applications with dependencies for consistent deployment
   - Container orchestration (Kubernetes) for management at scale
   - Influences architecture through service boundaries and deployment units
   - Benefits: consistency, isolation, resource efficiency, scalability
   - Drawbacks: operational complexity, potential security concerns

## Architecture Governance

1. **Architecture Review Boards**
   - Cross-functional team that evaluates and approves architectural decisions
   - Ensures alignment with enterprise standards and strategies
   - Provides guidance and mentoring on architectural practices

2. **Reference Architectures**
   - Standardized architecture for a specific domain or organization
   - Provides templates, patterns, and guidance for implementations
   - Ensures consistency and best practices across projects

3. **Technical Debt Management**
   - Identifying, tracking, and addressing architectural compromises
   - Regular refactoring and architectural improvement
   - Balancing short-term needs with long-term architectural health

4. **Architecture Runway**
   - Creating architectural capabilities ahead of feature development
   - Ensures architecture can support upcoming functionality
   - Prevents architecture becoming a bottleneck to delivery
  
   ===
   ---
   ---


   `STUDY NOTE FROM PROFESSOR - FINAL EXAM - READING NOTES:`
   # I most read this today - Final Exam notes:





# CSC430 Final Exam Study Guide: Key Topics Explanation and Practice Questions

## 1. Software Development Life Cycle (SDLC)

### Explanation
SDLC stands for Software Development Life Cycle - a structured process that software development teams follow to design, develop, test, and deploy high-quality software. The phases typically include:

1. **Planning**: Identifying the scope, resources, timelines, and potential risks
2. **Analysis**: Gathering and documenting detailed requirements
3. **Design**: Creating software architecture and technical specifications
4. **Implementation/Development**: Writing code based on the design documents
5. **Testing**: Verifying the software works as expected and is free of defects
6. **Deployment**: Releasing the software to users
7. **Maintenance**: Providing ongoing support, updates, and enhancements

### Practice Questions
1. What does SDLC stand for and why is it important in software development?
2. During which SDLC phase would you create detailed technical specifications and software architecture?
3. Scenario: A development team completed coding but discovered numerous bugs during testing. Which SDLC phase was likely inadequately performed?
4. Which SDLC phase continues for the longest time in the product's life?

## 2. Requirement Documentation

### Explanation
Requirement documentation captures what the software system must do (functional requirements) and how it should perform (non-functional requirements).

**Functional Requirements**: Describe specific behaviors, features, and capabilities the system must perform.
- Example: "The system shall allow users to reset their password via email verification."

**Non-functional Requirements**: Specify quality attributes, constraints, and performance characteristics.
- Examples: Security requirements, performance metrics (response time), usability, reliability, compatibility

**Purpose**: 
- Creates a shared understanding between stakeholders and developers
- Provides a basis for project planning, estimation, and scheduling
- Serves as a contract for what will be delivered
- Used to validate the final product

### Practice Questions
1. How do functional requirements differ from non-functional requirements? Provide an example of each.
2. A requirement states: "The system must respond to user queries within 2 seconds." Is this functional or non-functional? Why?
3. What challenges might arise if requirement documentation is inadequate?
4. Scenario: A client complains that the delivered software doesn't meet their expectations despite following all documented requirements. What might have been the issue in the requirements process?

## 3. SOLID Principles

### Explanation
SOLID is an acronym for five design principles intended to make software designs more understandable, flexible, and maintainable:

- **S - Single Responsibility Principle**: A class should have only one reason to change (one responsibility)
- **O - Open/Closed Principle**: Software entities should be open for extension but closed for modification
- **L - Liskov Substitution Principle**: Objects of a superclass should be replaceable with objects of a subclass without affecting program correctness
- **I - Interface Segregation Principle**: Many client-specific interfaces are better than one general-purpose interface
- **D - Dependency Inversion Principle**: High-level modules should not depend on low-level modules; both should depend on abstractions

### Practice Questions
1. How does following the Single Responsibility Principle improve code maintainability?
2. Explain how the Open/Closed Principle allows for software evolution without breaking existing functionality.
3. Which SOLID principle is violated when a subclass doesn't properly implement methods from its parent class, causing unexpected behavior?
4. Scenario: A developer creates a single large interface that all classes must implement, even though many classes only use a small subset of the methods. Which SOLID principle is being violated?

## 4. Development Methodologies Comparison

### Explanation

**Waterfall**:
- Sequential, linear approach where each phase must be completed before the next begins
- Phases: Requirements, Design, Implementation, Verification, Maintenance
- Advantages: Simple to understand and manage, well-defined milestones
- Disadvantages: Inflexible to changes, customer sees product only at the end

**Agile**:
- Iterative approach with continuous feedback
- Emphasizes flexibility, customer collaboration, and responding to change
- Features delivered in small, frequent increments
- Advantages: Adaptable to changing requirements, frequent customer feedback
- Disadvantages: Can lose focus without proper management, less predictable

**Extreme Programming (XP)**:
- Agile methodology focused on technical excellence and customer satisfaction
- Key practices: Pair programming, test-driven development, continuous integration, simple design, refactoring
- Advantages: High-quality code, rapid feedback, improved teamwork
- Disadvantages: Requires significant discipline, may not scale well for all teams

### Practice Questions
1. How does the approach to requirements differ between Waterfall and Agile methodologies?
2. What makes Extreme Programming different from other Agile methodologies?
3. In which development methodology would a complete requirements document be necessary before any design work begins?
4. Scenario: A project has rapidly changing requirements and stakeholders want frequent updates on progress. Which methodology would be most appropriate and why?

## 5. UML Diagrams

### Explanation

**Class Diagram**:
- Shows the static structure of a system - classes, attributes, methods, and relationships
- Relationships include: Association, Aggregation, Composition, Inheritance, Implementation
- Used for: Modeling the object-oriented view of a system, showing class hierarchies, defining relationships

**Sequence Diagram**:
- Shows object interactions arranged in time sequence
- Depicts which operations happen between which objects and in what order
- Used for: Modeling the dynamic behavior of the system, showing the flow of messages between objects, describing complex interactions

**Drawing a Simple Class Diagram**:
- Classes represented as rectangles divided into 3 sections (name, attributes, methods)
- Relationships shown as lines with specific notation (arrows, diamonds)
- Visibility modifiers (+public, -private, #protected)

### Practice Questions
1. What type of UML diagram would you use to model the inheritance hierarchy of classes in a system?
2. How does a sequence diagram differ from a class diagram in terms of what it represents?
3. Draw a simple class diagram for a basic library system with Book, Author, and Library classes. Show appropriate relationships and key attributes/methods.
4. Scenario: You need to visualize how a user login process works, showing interactions between the user interface, authentication service, and database. Which UML diagram would be most appropriate?

## 6. Cohesion and Coupling

### Explanation

**Cohesion**:
- Measures how strongly related the responsibilities of a single module are
- High cohesion (desirable): A module performs a single, well-defined task
- Low cohesion (undesirable): A module performs multiple unrelated functions

**Coupling**:
- Measures how dependent modules are on each other
- Loose coupling (desirable): Modules interact with minimal knowledge of each other's internal workings
- Tight coupling (undesirable): Changes in one module require changes in other modules

**Goal**: Software should have high cohesion and low coupling for better maintainability, testability, and reusability.

### Practice Questions
1. Why is high cohesion desirable in software design?
2. How does loose coupling benefit software maintenance?
3. A class named "Utility" contains methods for database access, email formatting, and mathematical calculations. Is this an example of high or low cohesion? Explain.
4. Scenario: Two modules need to be modified every time a database schema changes. What does this indicate about the coupling in the system?

## 7. Four Security Principles

### Explanation

**Confidentiality**:
- Ensuring information is accessible only to those authorized to access it
- Implemented through encryption, access controls, and authentication

**Integrity**:
- Ensuring information is accurate, complete, and has not been tampered with
- Implemented through checksums, digital signatures, and access controls

**Availability**:
- Ensuring information and systems are available when needed
- Implemented through redundancy, backups, and disaster recovery planning

**Non-repudiation**:
- Ensuring that a party cannot deny the authenticity of their signature or sending a message
- Implemented through digital signatures, audit trails, and timestamps

### Practice Questions
1. Which security principle is violated if an unauthorized user can view sensitive customer data?
2. How does a DDoS attack specifically target which security principle?
3. If a system uses checksums to verify that data hasn't been altered, which security principle is being enforced?
4. Scenario: A bank's transaction system goes down for maintenance during business hours without prior notice. Which security principle is compromised?

## 8. Design Patterns

### Explanation
Design patterns are proven solutions to common software design problems. They provide templates for how to solve problems that occur repeatedly.

**Creational Patterns**: Deal with object creation mechanisms
- Examples: Singleton, Factory Method, Abstract Factory, Builder, Prototype

**Structural Patterns**: Deal with object composition and relationships
- Examples: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy

**Behavioral Patterns**: Deal with object communication and responsibility
- Examples: Observer, Strategy, Command, Template Method, Iterator, State

**Benefits**:
- Provides proven solutions to common problems
- Creates a common language for developers
- Promotes code reuse and maintainability
- Encapsulates varying parts of a system

### Practice Questions
1. Why are design patterns valuable in software development?
2. Which design pattern would you use when you need exactly one instance of a class throughout the application?
3. How does the Observer pattern facilitate loose coupling between objects?
4. Scenario: You need to integrate a new third-party payment processing library with a different interface than your system expects. Which design pattern would help solve this problem?

## 9. Product Support Life Cycle

### Explanation
The Product Support Life Cycle defines the stages a software product goes through from initial release to retirement:

1. **Introduction**: Initial release with core functionality
2. **Growth**: Adding features, expanding user base
3. **Maturity**: Stable product, minor enhancements, bug fixes
4. **Decline**: Reduced support, fewer updates
5. **End of Life/Retirement**: No further support or development

Support activities include:
- Bug fixes and patches
- Security updates
- Feature enhancements
- Technical support
- Documentation updates

### Practice Questions
1. What characterizes the maturity phase of the product support life cycle?
2. Why is it important to communicate end-of-life dates to customers?
3. How do support requirements differ between the growth and decline phases?
4. Scenario: A company has a 10-year-old software product with declining sales but a significant base of loyal users. What considerations should be made regarding the product's support life cycle?

## 10. Key Terms

### Explanation

**Authentication vs. Authorization**:
- **Authentication**: Verifying the identity of a user (who you are)
- **Authorization**: Determining what actions an authenticated user is allowed to perform (what you can do)

**Test Case**: A set of conditions, inputs, and expected results designed to verify specific functionality

**Sprint**: A fixed time period (usually 2-4 weeks) in Agile where a set of work is completed and ready for review

**Scrum Meeting**: Daily short meeting where team members discuss what they did yesterday, what they'll do today, and any blockers

**User Story**: A simple description of a feature from the end user's perspective, typically following the format "As a [role], I want [feature] so that [benefit]"

**Roles**:
- **QA**: Responsible for testing software and ensuring quality
- **Tech Lead**: Provides technical guidance and makes architecture decisions
- **Developers**: Write and maintain code
- **Product Owner**: Represents customer needs and prioritizes features

**Problem-Resolution Cycle**: The process of identifying, analyzing, resolving, and verifying fixes for software issues

**STAR (Situation, Task, Action, Result)**: A structured method for answering behavioral interview questions

**Risk Matrix**: A tool to assess risks based on probability and impact

**DREAD (Damage, Reproducibility, Exploitability, Affected users, Discoverability)**: A model for assessing security risks

### Practice Questions
1. Differentiate between authentication and authorization with an example of each.
2. What is the purpose of the daily scrum meeting and what three questions should team members answer?
3. How does a product owner contribute to the success of an agile project?
4. In the context of a risk matrix, how would you classify a highly impactful but unlikely risk?
5. How does DREAD help in prioritizing security vulnerabilities?

## Final Exam Practice Questions

### Multiple Choice
1. Which SDLC phase involves creating detailed technical specifications and software architecture?
   a) Planning
   b) Analysis
   c) Design
   d) Implementation

2. The statement "A class should have only one reason to change" describes which SOLID principle?
   a) Single Responsibility Principle
   b) Open/Closed Principle
   c) Liskov Substitution Principle
   d) Dependency Inversion Principle

3. Which design pattern ensures that a class has only one instance and provides a global point of access to it?
   a) Factory
   b) Builder
   c) Singleton
   d) Observer

4. Which security principle is concerned with protecting data from unauthorized changes?
   a) Confidentiality
   b) Integrity
   c) Availability
   d) Non-repudiation

### Fill in the Blanks
1. The ____________ diagram shows the static structure of a system, including classes, attributes, and methods.
2. Software with high ____________ has modules that perform single, well-defined tasks.
3. The ____________ principle states that software entities should be open for extension but closed for modification.
4. In Agile methodologies, a fixed time period in which specific work must be completed is called a ____________.

### Short Answers
1. Explain the difference between functional and non-functional requirements with an example of each.
2. Describe how the Observer design pattern works and provide a real-world example of its use.
3. What are the benefits of using test cases in software development?
4. How does the Agile methodology differ from Waterfall in terms of customer involvement?

### Matching
Match the design pattern with its description:

1. Singleton     A. Defines a family of algorithms and makes them interchangeable
2. Adapter       B. Ensures a class has only one instance
3. Observer      C. Allows incompatible interfaces to work together
4. Strategy      D. Defines a one-to-many dependency between objects

### Scenario-Based Questions
1. A software project has well-defined, stable requirements, and the customer wants detailed documentation before development begins. Which development methodology would be most appropriate and why?

2. You're designing a system where one object needs to notify multiple other objects when its state changes, without knowing which objects are observing it. Which design pattern would you use and how would you implement it?

3. Your team is developing an e-commerce application and needs to ensure that customer payment information is protected from unauthorized access and that transactions cannot be denied by customers later. Which security principles should be prioritized and what measures could be implemented?

4. You notice that whenever you change the database structure in your application, you have to modify code in both the UI and business logic layers. What does this indicate about your system's design, and how might you improve it?

These explanations and practice questions should help you prepare thoroughly for your final exam. Focus on understanding the concepts rather than memorizing definitions, as scenario-based questions will require applying your knowledge to specific situations.



# Answers to CSC430 Final Exam Practice Questions

## Multiple Choice Answers

1. Which SDLC phase involves creating detailed technical specifications and software architecture?
   **Answer: c) Design**
   *Explanation: The Design phase of the SDLC is where software architecture and technical specifications are created, before actual coding begins in the Implementation phase.*

2. The statement "A class should have only one reason to change" describes which SOLID principle?
   **Answer: a) Single Responsibility Principle**
   *Explanation: The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning it should have only one responsibility or job.*

3. Which design pattern ensures that a class has only one instance and provides a global point of access to it?
   **Answer: c) Singleton**
   *Explanation: The Singleton pattern restricts instantiation of a class to one single instance and provides a global point of access to that instance throughout the application.*

4. Which security principle is concerned with protecting data from unauthorized changes?
   **Answer: b) Integrity**
   *Explanation: Integrity in security ensures that information is accurate, complete, and has not been tampered with by unauthorized parties.*

## Fill in the Blanks Answers

1. The **class** diagram shows the static structure of a system, including classes, attributes, and methods.
   *Explanation: Class diagrams in UML represent the static structure of a system by showing classes, their attributes, methods, and relationships between classes.*

2. Software with high **cohesion** has modules that perform single, well-defined tasks.
   *Explanation: High cohesion means a module or class has a clear, focused purpose and all its elements contribute to a single well-defined function.*

3. The **Open/Closed** principle states that software entities should be open for extension but closed for modification.
   *Explanation: The Open/Closed Principle (OCP) states that software entities should be extendable without modifying their existing code.*

4. In Agile methodologies, a fixed time period in which specific work must be completed is called a **sprint**.
   *Explanation: A sprint is a time-boxed period (usually 2-4 weeks) during which a specific set of work must be completed and made ready for review in Agile methodologies, particularly Scrum.*

## Short Answers

1. **Explain the difference between functional and non-functional requirements with an example of each.**

   Functional requirements describe what the system should do, specifying specific behaviors, features, or functions that the system must perform. They define the system's capabilities.
   *Example: "The system shall allow users to reset their password via email verification."*

   Non-functional requirements describe how the system should perform, focusing on quality attributes, constraints, and performance characteristics rather than specific behaviors.
   *Example: "The system must respond to user queries within 2 seconds under normal load conditions."*

2. **Describe how the Observer design pattern works and provide a real-world example of its use.**

   The Observer pattern defines a one-to-many dependency between objects, where when one object (the subject) changes state, all its dependents (observers) are notified and updated automatically. The pattern involves:
   - A subject interface that allows attaching, detaching, and notifying observers
   - A concrete subject that maintains state and notifies observers when state changes
   - An observer interface that defines the update method
   - Concrete observer classes that respond to updates

   *Real-world example: A news subscription service where subscribers (observers) receive notifications whenever new articles (state changes) are published by the news service (subject). Each subscriber automatically receives updates without the news service needing to know details about them.*

3. **What are the benefits of using test cases in software development?**

   Benefits of test cases include:
   - Verifying that software meets requirements and functions correctly
   - Providing a way to systematically identify and fix defects
   - Creating a repeatable validation process that can be run after changes
   - Serving as documentation of expected system behavior
   - Enabling regression testing to ensure new changes don't break existing functionality
   - Improving code quality and reducing maintenance costs
   - Facilitating communication between testers, developers, and stakeholders by clearly defining expected behavior

4. **How does the Agile methodology differ from Waterfall in terms of customer involvement?**

   In Waterfall, customer involvement is primarily front-loaded and end-loaded. Customers are heavily involved during the initial requirements gathering phase and then again during final acceptance testing, with limited interaction during the development phases.

   In Agile, customer involvement is continuous throughout the development process. A customer representative (often the Product Owner) is regularly engaged, reviews work at the end of each iteration (sprint), provides feedback, and participates in prioritizing features for upcoming iterations. This continuous involvement allows for adjustments based on changing requirements or feedback, creating a more collaborative and responsive development process.

## Matching Answers

1. Singleton - **B. Ensures a class has only one instance**
2. Adapter - **C. Allows incompatible interfaces to work together**
3. Observer - **D. Defines a one-to-many dependency between objects**
4. Strategy - **A. Defines a family of algorithms and makes them interchangeable**

## Scenario-Based Question Answers

1. **A software project has well-defined, stable requirements, and the customer wants detailed documentation before development begins. Which development methodology would be most appropriate and why?**

   **Answer: Waterfall methodology would be most appropriate for this scenario.**

   *Explanation: Waterfall is well-suited for projects with stable, well-understood requirements that are unlikely to change significantly. Since the requirements are well-defined and the customer desires detailed documentation before development begins, Waterfall's sequential approach would work well. Waterfall emphasizes comprehensive documentation at each phase and requires sign-off before proceeding to the next phase, which aligns with this customer's preferences. The predictable nature of Waterfall also makes it easier to estimate timelines and resources for projects where the scope is clearly defined from the start.*

2. **You're designing a system where one object needs to notify multiple other objects when its state changes, without knowing which objects are observing it. Which design pattern would you use and how would you implement it?**

   **Answer: The Observer design pattern would be most appropriate for this scenario.**

   *Implementation approach:*
   1. Create a Subject interface with methods for attaching, detaching, and notifying observers
   2. Implement a ConcreteSubject class that maintains a list of observers and calls their update methods when its state changes
   3. Define an Observer interface with an update method
   4. Implement ConcreteObserver classes that register with the subject and implement the update method to respond to changes

   *This pattern allows for loose coupling because the subject knows only that its observers implement a common interface; it doesn't need to know their concrete classes. Observers can be added or removed at runtime without modifying the subject. The pattern is particularly useful for implementing distributed event handling systems and is commonly used in MVC architectures where the model (subject) notifies views (observers) when data changes.*

3. **Your team is developing an e-commerce application and needs to ensure that customer payment information is protected from unauthorized access and that transactions cannot be denied by customers later. Which security principles should be prioritized and what measures could be implemented?**

   **Answer: The security principles of Confidentiality, Integrity, and Non-repudiation should be prioritized.**

   *Measures to implement:*
   
   *For Confidentiality (protecting payment information from unauthorized access):*
   - Encrypt sensitive data both in transit using TLS/SSL and at rest using strong encryption algorithms
   - Implement strong access controls and authentication mechanisms
   - Follow PCI-DSS compliance requirements for handling credit card information
   - Use tokenization to replace sensitive data with non-sensitive equivalents
   
   *For Integrity (ensuring data isn't tampered with):*
   - Implement data validation and sanitization
   - Use checksums or hash functions to verify data integrity
   - Apply proper input validation to prevent SQL injection and other attacks
   
   *For Non-repudiation (ensuring customers cannot deny making transactions):*
   - Implement digital signatures for transactions
   - Maintain comprehensive audit logs of all transactions
   - Use multi-factor authentication for payment confirmation
   - Send confirmation emails or messages that the customer must acknowledge
   - Store timestamps and IP addresses associated with transactions

4. **You notice that whenever you change the database structure in your application, you have to modify code in both the UI and business logic layers. What does this indicate about your system's design, and how might you improve it?**

   **Answer: This indicates tight coupling between layers and a violation of separation of concerns in the system's design.**

   *The problem:* Changes to the database structure should ideally be isolated to the data access layer, but in this case, they're cascading to multiple layers. This suggests that implementation details of the database are leaking into other parts of the application, creating unnecessary dependencies.

   *Improvements:*
   
   1. Implement a layered architecture with clear separation of concerns:
      - Data Access Layer to handle database interactions
      - Business Logic Layer for processing and rules
      - Presentation Layer for UI elements
   
   2. Use abstraction and dependency inversion:
      - Create interfaces or abstract classes to decouple higher-level modules from lower-level modules
      - Make both UI and business logic depend on abstractions rather than concrete implementations
   
   3. Implement a repository pattern to abstract database access:
      - Create repositories that provide a collection-like interface for accessing data
      - Use DTOs (Data Transfer Objects) or domain objects that are independent of database structure
   
   4. Consider using an ORM (Object-Relational Mapping) tool:
      - This can abstract the database details and reduce the impact of structural changes
   
   5. Apply the Adapter pattern:
      - Create adapters that translate between the database models and the models used by the business logic
   
   These improvements would lead to looser coupling between system components, making the system more maintainable and adaptable to changes.
