import random

DIFFICULTY_FLAVOR = {
    "Easy": {
        "taglines": [
            "A gentle path begins.",
            "Fortune favors the bold... and the curious.",
            "The winds are warm and kind.",
            "Learn the rhythm, feel the steel."
        ],
        "warnings": [
            "Enemies are forgiving; mistakes won't be fatal-yet.",
            "A safe road... but darkness still watches."
        ],
        "lore": [
            "The village torchlight still reaches this trail.",
            "Old stones whisper names of beginners turned heroes."
        ],
        "voice": {
            "Warrior": [
                "Every blade starts dull. Let's sharpen."
            ],
            "Mage": [
                "A calm current-perfect for practice."
            ],
            "Archer": [
                "Soft breeze. Easy marks."
            ],
            "Priest": [
                "Mercy guides our steps"
            ]
        }
    },
    "Normal": {
        "taglines": [
            "Balance of peril and promise.",
            "The road narrows; the stakes rise.",
            "Shadows lengthen beside your stride.",
            "Glory weighs as much as danger."
        ],
        "warnings": [
            "You'll need wits and timing-no passengers."
        ],
        "lore": [
            "Trails of iron prints and faded banners mark this route.",
            "Echos of skirmishes rattle in the hedgerows."
        ],
        "voice": {
            "Warrior": ["Now we're talking."],
            "Mage": ["Equations of risk... solvable."],
            "Archer": ["Targets won't stand still this time."],
            "Priest": ["I'll keep you standing. Mostly"]
        }
    },
    "Hard": {
        "taglines": [
            "Only the steady survive the storm.",
            "Missteps echo loudly here.",
            "Steel meets sorcery-and blinks first.",
            "The dark answers back."
        ],
        "warnings": [
            "Healing is scarce; enemies punish greed.",
            "Retreat is wisdom; stubbornness is a headstone."
        ],
        "lore": [
            "Crows memorize the names carved in these milestones.",
            "The mud remembers fallen boots-and keeps them."
        ],
        "voice": {
            "Warrior": ["At last, a worthy ache."],
            "Mage": ["The arcane bites if mishandled."],
            "Archer": ["Wind's against us-good"],
            "Priest": ["I can mend bones, not pride"]
        }
    },
    "Nightmare": {
        "taglines": [
            "Abandon comfort, not courage.",
            "The Dark Wizard hears your heartbeat.",
            "Where legends fail-and myths are born.",
            "Light is a loan you must repay."
        ],
        "warnings": [
            "Death is a teacher with cruel tuition.",
            "Few return. Fewer boast."
        ],
        "lore": [
            "The sky here is stitched with thunder.",
            "Maps refuse to ink these lands."
        ],
        "voice": {
            "Warrior": ["Chain the fear. Break the rest."],
            "Mage": ["Spellbooks smolder under this pressure."],
            "Archer": ["One breath. One shot. No mercy."],
            "Priest": ["If faith falters, hold the line anyway."]
        }
    }
}

def pick_lines(difficulty: str, hero_class: str):
    d = DIFFICULTY_FLAVOR[difficulty]
    return {
        "tagline": random.choice(d["taglines"]),
        "warning": random.choice(d["warnings"]),
        "lore": random.choice(d["lore"]),
        "voice": random.choice(d["voice"].get(hero_class, ["..."]))
    }