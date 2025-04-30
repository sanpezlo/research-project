from tag import TAGS, Tag
from group import Group


def transpile(problem: dict[Tag, list[list[Group]]], tag: Tag) -> list[str]:
    flags = [flag for flag in Tag if flag in tag]
    combinations: list[str] = []
    if (len(flags) < 2):
        for block in problem[tag]:
            for i, group in enumerate(block):
                result = Group.join(problem[Tag.CORRECT][0][i], group)
                combinations += Group.combine(result)
    else:
        before = [problem[Tag.CORRECT][0]]
        for flag in flags:
            temp_tag: list[list[Group]] = []
            for before_block in before:
                for block in problem[flag]:
                    temp_block: list[Group] = []
                    for i, group in enumerate(block):
                        temp_block.append(Group.join(before_block[i], group))
                    temp_tag.append(temp_block)
            before = temp_tag
        for block in before:
            for i, group in enumerate(block):
                combinations += Group.combine(group)
    return combinations
