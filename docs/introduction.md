# Introduction

**What?**

In this project there are so many concepts of DDD but its no a complete implemetation of DDD.

**Why?**

Because there are only 20 use cases and life its too short to overengineer in all projects.

**How?**

- Articles `Aggregate Root`
  - Tags `Value-Object`
  - Commnets `Entity`
- Users `Aggregate Root`
  - Profile `Value-Object`

## Project Schema

```
src
├── api
│   ├── healthcheck.py
│   └── v1
│       ├── dtos
│       ├── articles.py
│       └── users.py
├── application
│   ├── articles           <= App Module
│   │   ├── factory.py     <= Factory to create an Articles Module
│   │   ├── domain         <= Domain layer and abstract repositories
│   │   ├── infrastructure <= Implementation of repositories
│   │   └── use_cases      <= Use Cases
│   └── users              <= App Module
│       ├── factory.py
│       ├── domain
│       ├── infrastructure
│       └── use_cases
├── cmd
│   ├── commands.py
│   └── subcommands.py
├── config.py
├── factories.py
├── main.py
└── shared
    ├── domain
    │   ├── errors
    │   ├── events
    │   ├── hex
    │   └── value_objects
    └── utils
        └── generate_uuid.py
```
