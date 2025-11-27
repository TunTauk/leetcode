from typing import List
from collections import Counter
from functools import lru_cache


class Solution:

    def minStickers(self, stickers: List[str], target: str) -> int:
        target_dict = Counter(target)
        sticker_dicts: List[Counter[str]] = []

        for sticker in stickers:
            sticker_dict = Counter(sticker)
            for key in sticker_dict.keys():
                if target_dict[key] > 0:
                    sticker_dicts.append(sticker_dict)
                    break

        for key in target_dict.keys():
            has_key = False
            for sticker_dict in sticker_dicts:
                if sticker_dict[key] > 0:
                    has_key = True
                    break
            if not has_key:
                return -1

        @lru_cache(maxsize=None)
        def removeSticker(target: str) -> int:
            if not target:
                return 0
            counts = []
            for sticker_dict in sticker_dicts:
                rm_dict = Counter(target) - sticker_dict
                remaining = "".join(
                    sorted([ch for ch, v in rm_dict.items() for _ in range(v)])
                )
                if remaining != target:
                    c = removeSticker(remaining) + 1
                    counts.append(c)
            return min(counts)

        return removeSticker("".join(sorted(target)))


s = Solution()
print(
    s.minStickers(
        [
            "indicate",
            "why",
            "finger",
            "star",
            "unit",
            "board",
            "sister",
            "danger",
            "deal",
            "bit",
            "phrase",
            "caught",
            "if",
            "other",
            "water",
            "huge",
            "general",
            "read",
            "gold",
            "shall",
            "master",
            "men",
            "lay",
            "party",
            "grow",
            "view",
            "if",
            "pull",
            "together",
            "head",
            "thank",
            "street",
            "natural",
            "pull",
            "raise",
            "cost",
            "spoke",
            "race",
            "new",
            "race",
            "liquid",
            "me",
            "please",
            "clear",
            "could",
            "reply",
            "often",
            "huge",
            "old",
            "nor",
        ],
        "fhhfiyfdcwbycma",
    )
)
# print(s.minStickers(stickers=["with", "example", "science"], target="thehat"))
# print(s.minStickers(stickers = ["notice","possible"], target = "basicbasic"))
