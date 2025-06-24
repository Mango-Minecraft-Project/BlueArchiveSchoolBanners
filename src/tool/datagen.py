import json

from global_variable import GENERATED, NAMESPACE, BANNER_PATTERN, COLORS, make_dir

DATA = make_dir(GENERATED / "data", rmdir=True)
DATA_WITH_NAMESPACE = make_dir(DATA / NAMESPACE)

with open(
    make_dir(DATA / "minecraft/tags/banner_pattern") / "no_item_required.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        {
            "replace": False,
            "values": [f"{NAMESPACE}:{pattern}" for pattern in BANNER_PATTERN],
        },
        file,
        indent=4,
        ensure_ascii=False,
    )

for pattern in BANNER_PATTERN:
    with open(
        make_dir(DATA_WITH_NAMESPACE / "banner_pattern") / f"{pattern}.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            {
                "asset_id": f"{NAMESPACE}:{pattern}",
                "translation_key": f"block.minecraft.banner.{NAMESPACE}.{pattern}",
            },
            file,
            indent=4,
            ensure_ascii=False,
        )

RESOURCE_WITH_NAMESPACE = make_dir(make_dir(GENERATED / "assets", rmdir=True) / NAMESPACE)

with open(
    make_dir(RESOURCE_WITH_NAMESPACE / "lang") / "en_us.json", "w", encoding="utf-8"
) as file:
    json.dump(
        {
            f"block.minecraft.banner.{NAMESPACE}.{pattern}.{color}": f"{color.title()} {pattern.title()}"
            for pattern in BANNER_PATTERN
            for color in COLORS
        },
        file,
        indent=4,
        ensure_ascii=False,
    )
