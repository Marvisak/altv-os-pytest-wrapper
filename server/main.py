from typing import List

import platform
import pytest
import alt


def test_resource(resource: alt.Resource, args: List[str]) -> None:
    # On Windows we need to add flag --capture=sys, so that pytest doesn't use the file descriptors
    if platform.system() == "Windows":
        if "--capture=fd" in args:
            alt.log_error(
                "You have --capture=fd in your arguments, this breaks the resource on Windows, please remove it"
            )
        args.insert(0, "--capture=sys")

    args.append(resource.path)
    pytest.main(args)


def handle_pytest_command(args: List[str]) -> None:
    if args:
        resource_name = args[-1]
        resource = alt.Resource.get_by_name(resource_name)
        if resource:
            args.remove(resource_name)
            test_resource(resource, args)
            return

    resources = alt.Resource.all
    for resource in resources:
        test_resource(resource, args)


@alt.event(alt.Event.ConsoleCommand)
def console_command(cmd: str, args: List[str]) -> None:
    if cmd == "pytest":
        handle_pytest_command(args)
