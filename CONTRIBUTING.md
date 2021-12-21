# Contributing Guide

This project is completely open-sourced, and we welcome all kind of contributions. This is to in order to
enforce clean code, and to ensure the quality of the code we write is maintained.

We have strict guidelines for people who are willing or looking to contribute to this project. Please read them carefully. The contributions may be rejected on the basis of a contributor failing to follow these guidelines.

## The Golden Rules of Contributing

1. **Lint before you push.** We have simple but strict style of rules that are enforced through linting. You must
   always lint your code before committing or pushing. Using tools such as `flake8` and `pre-commit` can make this
   easier. Make sure to follow our [style guide](./CONTRIBUTING.md#style-guide) when contributing.
2. **Make great commits.** Great commits should be atomic, with a commit message explaining what and why. More on this can be found in [this section](./CONTRIBUTING.md#writing-good-commit-messages).
3. **Do not open a pull request if you aren't assigned to the issue.** If someone is already working on some
   issue, consider offering to collaborate instead of working on your own.
   Feel free to ask to be assigned to the issue, if nobody is working on it, or assigned. Before working on a
   totally new feature, change or anything, create an issue to notify, and get assigned to it first. This helps
   us to keep the PRs under control and to make sure if we have the need, or use for it in our codebase. By
   closing and declining it, we save time and energy for both of us.
4. **Use assets which are licensed for public use.** Whenever any code snippets, or static assets such as image,
   video, audio or files are added, they must have a compatible license with our projects.
5. **Follow our [Code of Conduct](./CODE_OF_CONDUCT.md).** We aim to foster an open, welcoming and friendly
   environment. Please read our [Code of Conduct](./CODE_OF_CONDUCT.md) before contributing.

## Writing Good Commit Messages

A well-structured git log is key to a project's maintainability; it provides insight into when and why things
were done for future maintainers of the project.

Commits should be as narrow in scope as possible. Commits that span hundreds of lines across multiple
unrelated functions and/or files are very hard for maintainers to follow. After about a week they'll probably
be hard for you to follow, too.

Please also avoid making minor commits for fixing typos or linting errors. Use the linting feature using
Flake8 and Pre-commit scripts in Pipfile to lint them before pushing.

To get you started, Here's an incredible resource on how to make good commits!

- <https://chris.beams.io/posts/git-commit/>

## Linting and Pre-commit

We make use of `flake8` and `pre-commit` to ensure that the code style is consistent across the code base.

Running `flake8` will warn you about any potential style errors in your contribution. You must always check it before pushing. Your commit will be rejected by the build server if it fails to lint.

`pre-commit` is a powerful tool that helps you automatically lint before you commit. If the linter complains,
the commit is aborted so that you can fix the linting errors before committing again. That way, you never commit
the problematic code in the first place!

To make linting and checking easy, we have setup pipenv scripts to faciliate installing the commit hooks, and
running the lint checks.

Here is how you can setup pre-commit with ease:

1. Ensure that you have dependencies (and dev-dependencies) installed using pipenv.
2. Once you're ready, run `pipenv run precommit`, which install the precommit hooks to check your code style
   when you're commiting it. It stops code from getting commited, if issues are discovered.
3. Finally, To run the linting manually, just use `pipenv run lint`, and you should be good to go.

**Note**: If you really need to commit code, and fix the issues or take assistance, run `git commit --no-verify`
to skips the precommit checks.

## Style Guide

We have enforced several rules related to the code-style which we are following. They have been added
to ensure readable, clean and maintainable code is written, and enable working for everyone smooth and easy.

We use `flake8` to perform linting, and `pre-commit` to ensure the code is perfect, before getting pushed.

### Type Hinting

[PEP 484](https://www.python.org/dev/peps/pep-0484/) formally specifies type hints for Python functions, added
to the Python Standard Library in version 3.5. Type hints are recognized by most modern code editing tools and
provide useful insight into both the input and output types of a function, preventing the user from having to
go through the codebase to determine these types.

For an example, a function without annotations would look like:

```py
def divide(a, b):
    """Divide the two given arguments."""
    return a / b
```

With annotations, this is how the function would look:

```py
def divide(a: int, b: int) -> float:
    """Divide the two given arguments."""
    return a / b
```

Python type-hinting is relatively easy to use, but helps to keep the code more maintainable, clean, and also
enables the use of type annotations in the future. In a lot of situations, the type-hinting enables your editors
to give better intellisense and suggestions based on what you're working on.

Python being a dynamically typed language, There is a neat tool called MyPy that enables static type hinting
and checking on the code. You can read more about it [here](https://mypy.readthedocs.io/en/stable/).

### Docstring formatting directive

Many documentation packages provide support for automatic documentation generation from the codebase's docstrings.
These tools utilize special formatting directives to enable richer formatting in the generated documentation.

For example:

```py
import typing as t


def foo(bar: int, baz: t.Optional[t.Dict[str, str]] = None) -> bool:
    """
    Does some things with some stuff.

    :param bar: Some input
    :param baz: Optional, some dictionary with string keys and values

    :return: Some boolean
    """
    ...
```

Since we don't utilize automatic documentation generation, use of this syntax should not be used in the code contributed here.

Should the purpose and type of the input variables not be easily discernable from the variable name and type
annotation a prose explanation can be used. Explicit references to variables, function, classes, etc. should be
wrapped with backticks (`` ` ``), such as \`variable\`.

For example, the above docstring would become:

```py
import typing as t


def foo(bar: int, baz: t.Optional[t.Dict[str, str]] = None) -> bool:
    """
    Does some things with some stuff.

    This function takes an index, `bar` and checks for its presence in the database `baz`, passed as a dictionary.
    Returns `False` if `baz` is not passed or if `bar` wasn't found in `baz`.
    """
    ...
```

### Strings and Quotes

Preference is to use double-quotes (`"`) wherever possible. Single quotes should only be used for cases where it is
logical. Exceptions might include:

- Using a key string within an f-string: f"Today is {data['day']}".
- Using double quotes within a string: 'She said "oh dear" in response'

Multi-line strings or Docstrings should be ensured that it's wrapped in triple double quotes (`"""my string"""`).

Wildcard imports should be avoided.

### Work in Progress (WIP) PRs

When any PR is actively being worked on, and is not ready for merging, it should be marked as a WIP. This provides
both a visual and functional indicator that the PR is in a draft state, and is not ready for review or merge.

Github provides a feature of marking a PR as Draft to indicate that it is not ready for review or merge. This
feature should be utilized in place of the traditional method of prepending `[WIP]` to the PR title.

As stated earlier, **ensure that "Allow edits from maintainers" is checked**. This gives permission for maintainers to commit changes directly to your fork, speeding up the review process.

[Here](https://github.blog/2019-02-14-introducing-draft-pull-requests/) is all the info you need about Draft PRs
in Github.

## Changes to this Arrangement

Every kind of projects evolve over time, and these contributing guidelines are no different.

This document is open to any kind of contributions, and PRs. Feel free to contribute to this guideline by
adding, or changing anything, that you feel can change it, and improve it aswell.

## Credits

This contributing guidelines file was inspired by
[Python discord's Contributing Guidelines](https://github.com/python-discord/bot/blob/master/CONTRIBUTING.md).
