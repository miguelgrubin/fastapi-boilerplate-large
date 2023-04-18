# Introduction

**What?**

Its a blog example using hexagonal architecture using app modules. Oriented to Large Projects.

**Why?**

_Why Hexagonal Architecture?_

Ports and Adapters, decoupled, testing strategy, tracing errors. ToDo: Explain this

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
├── app
│   ├── blog
│   │   ├── application
│   │   │   └── use_cases                       <=  Use Cases
│   │   │       ├── __init__.py
│   │   │       ├── user_creator.py
│   │   │       └── user_logger.py
│   │   ├── domain
│   │   │   ├── article.py                      <=  Article Domain Model
│   │   │   ├── article_repository.py           <=  Article Abstract Repository
│   │   │   ├── errors                          <=  Blog Domain Errors (UserNotFound, UserAlreadyExits, ...)
│   │   │   ├── events                          <=  Blog Domain Events (ArticleCreated, UserFollowed, ...)
│   │   │   ├── event_types.py                  <=  Enum with all event types on Blog
│   │   │   ├── user.py                         <=  User Domain Model
│   │   │   └── user_repository.py              <=  User Abstract Repository
│   │   ├── factory.py                          <=  Factories to initialize a Blog module (server, services, repositories, ...)
│   │   ├── infrastructure
│   │   │   ├── mappers                         <=  Mappers to transform (DTO <=> Domain Model <=> ORM Model)
│   │   │   │   └── user_mapper.py
│   │   │   ├── server                          <=  HTTP Routing
│   │   │   │   ├── article_routes.py           <=  Article Routing
│   │   │   │   ├── user_dtos.py                <=  User DTO (Requests, responses, query args)
│   │   │   │   ├── user_error_handlers.py      <=  Error handling (DomainError => HTTP Error)
│   │   │   │   └── user_routes.py              <=  User Routing
│   │   │   └── storage                         <=  Repository Implementations
│   │   │       ├── article_repository_memory.py
│   │   │       ├── article_repository_mongodb.py
│   │   │       ├── user_repository_memory.py
│   │   │       └── user_repository_mongodb.py
│   │   └── types.py                            <=  Blog typing objects
│   └── shared                                  <=  Shared Module
│       ├── application
│       │   └── use_case.py                     <=  Base UseCase definition
│       ├── domain
│       │   ├── errors                          <=  Shared Domain Error
│       │   ├── events                          <=  Shared Domain Events
│       │   ├── services                        <=  Shared Abstract Services
│       ├── factory.py                          <=  Factories to initialize Shared module
│       ├── infrastructure
│       │   └── services                        <=  Shared Implemented Services
│       └── types.py                            <=  Shared Typing
├── config.py                                   <=  App Config
├── factories.py                                <=  Factories to initialize an App instance
└── main.py                                     <=  Entrypoint
```
