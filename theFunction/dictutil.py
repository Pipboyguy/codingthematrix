# Task 0.6.4
from typing import Any, List


def dict2list(dct: dict[Any], keylist: List[Any]) -> List[Any]:
    return [dct[k] for k in keylist]


def list2dict(L: List[Any], keylist: List[Any]) -> List[Any]:
    return {k: v for v, k in zip(L, keylist)}


def listrange2dict(L: List[Any]) -> dict[int:Any]:
    return list2dict(L, range(len(L)))
