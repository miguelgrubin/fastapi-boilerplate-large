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
Layers            || Components     || Testing Strategy
=========================================================================================
Presentation      || HTTP Routing   || Integration && E2E tests
 ↓ ↑              ||                ||
Application       || Use Cases      || Social Unit Testing (Use Cases + Domain)
 ↓ ↑              ||                ||
Domain            || Domain Models  || Solitary Unit Testing (single class or function)
 ↓ ↑              ||                ||
Infrastructure    || Repositories   || Integration testing
```

## Project Schema

```
src
├── api                                  <=  HTTP Routing
│   ├── healthcheck.py                   <= Router to check http server
│   └── v1
│       ├── dtos                         <= DTO (Request, response, query args)
│       ├── articles.py                  <= Router for articles
│       └── users.py                     <= Router for users
├── app
│   └── blog                             <= AppModule
│       ├── domain
│       │   ├── errors                   <= Domain Errors
│       │   ├── events                   <= Domain Events
│       │   ├── article.py               <= Domain Model
│       │   ├── article_repository.py    <= Abstract Repository
│       │   ├── user.py                  <= Domain Model
│       │   └── user_repository.py       <= Abstract Repository
│       ├── infrastructure               <= Implemented Repositories
│       │   ├── article_memory_repository.py
│       │   ├── article_mongodb_repository.py
│       │   ├── article_sql_repository.py
│       │   ├── user_memory_repository.py
│       │   ├── user_mongodb_repository.py
│       │   └── user_sql_repository.py
│       ├── use_cases                    <= Use Cases
│       └── factory.py                   <= Factory to create an AppModule
├── cmd
│   ├── commands.py                      <= App Commands (./main.py server)
│   └── subcommands.py                   <= App Subcommands (./main.py create user)
├── config.py                            <= App Config
├── factories.py                         <= Factories to initialize an App instance
├── main.py                              <= Entripoint
└── shared
    ├── domain
    │   ├── events
    │   │   ├── domain_event.py
    │   │   └── event_types.py
    │   └── domain_model.py
    └── use_case.py
```
