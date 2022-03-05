# Introduction

**What?**

Its a blog example using hexagonal architecture using app modules. Oriented to Large Projects.

**Why?**

_Why Hexagonal Architecture?_

Ports and Adapters, decoupled, testing strategy, tracing errors. ToDo: Explain this

_Why not preventive DDD?_

You Aren't Gonna Need It (YAGNI) if your project is datacentric, CRUDy or your domain layer is not really complex.
And becouse life its too short to overengineer in all projects.

**How?**

```
Presentation      => HTTP Routers, ErrorHandlers, Middlewares, CLI commands <= Integration and E2E testing
 ↓ ↑
Application       => Use Cases <= Social Unit Testing (Application + Domain)
 ↓ ↑
Domain            => DomainModels, AbstractRepositories, Events, Errors <= Solitary Unit Testing (single class or function)
 ↓ ↑
Infrastructure    => Repositories <= Integration testing
```

- Blog `App Module`
  - Articles `DomainModel`
  - Users `DomainModel`

## Project Schema

```
src
├── api
│   ├── healthcheck.py        <= Router to check http server
│   └── v1
│       ├── dtos              <= DTO (Request, response, query args)
│       └── blog.py           <= Routes for Blog BC
├── app
│   └── blog                  <= AppModule
│       ├── factory.py        <= Factory to create an AppModule
│       ├── domain            <= Domain layer (DomainModels, Errors, Events, Abstract Repositories)
│       ├── infrastructure    <= Ifrastructure layer (Repositories)
│       └── use_cases         <= Application Layer (Use Cases)
├── cmd
│   ├── commands.py           <= App Commands (./main.py server)
│   └── subcommands.py        <= App Commands (./main.py create user)
├── config.py                 <= App Config
├── factories.py              <= Factories to initialize an App instance
├── main.py                   <= Entripoint
└── shared             Todo: refresh
    ├── domain
    │   ├── errors
    │   ├── events
    │   └── hex
    └── utils
        └── generate_uuid.py
```
