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
