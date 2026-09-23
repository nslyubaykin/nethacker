# heuristic monster types lists
# hypothesis: treating petrifying monsters as ranged-only prevents otherwise fatal
# contact attacks while preserving safe ranged and wand attacks.
ONLY_RANGED_SLOW_MONSTERS = ['floating eye', 'blue jelly', 'brown mold', 'gas spore', 'acid blob',
                             'chickatrice', 'cockatrice']
# hypothesis: keeping an unarmed barbarian in combat long enough to retreat
# from a visible contact-petrifier prevents exploration from pathing into a
# cockatrice or chickatrice when no safe ranged attack is available.
PETRIFYING_MONSTERS = ['chickatrice', 'cockatrice']
EXPLODING_MONSTERS = ['yellow light', 'gas spore', 'flaming sphere', 'freezing sphere', 'shocking sphere']
# hypothesis: treating common early multi-attack monsters as dangerous at a
# larger safety margin lets every barbarian retreat before one melee turn can
# consume its remaining hit points.
DANGEROUS_MONSTERS = ['giant ant', 'killer bee', 'soldier ant', 'fire ant', 'giant beetle', 'queen bee',
                      'jaguar', 'leocrotta', 'tiger', 'owlbear', 'mumak',
                      'rothe', 'large kobold', 'werejackal', 'wererat']
WEAK_MONSTERS = ['lichen', 'newt', 'shrieker', 'grid bug']
WEIRD_MONSTERS = ['leprechaun', 'nymph']


def is_monster_faster(agent, monster):
    _, y, x, mon, _ = monster
    # TOOD: implement properly
    return 'bat' in mon.mname or 'dog' in mon.mname or 'cat' in mon.mname \
           or 'kitten' in mon.mname or 'pony' in mon.mname or 'horse' in mon.mname \
           or 'bee' in mon.mname or 'fox' in mon.mname


def imminent_death_on_melee(agent, monster):
    if is_dangerous_monster(monster):
        return agent.blstats.hitpoints <= 24
    return agent.blstats.hitpoints <= 8


def is_dangerous_monster(monster):
    _, y, x, mon, _ = monster
    is_pet = 'dog' in mon.mname or 'cat' in mon.mname or 'kitten' in mon.mname or 'pony' in mon.mname \
             or 'horse' in mon.mname
    # 'mumak' in mon.mname or 'orc' in mon.mname or 'rothe' in mon.mname \
    # or 'were' in mon.mname or 'unicorn' in mon.mname or 'elf' in mon.mname or 'leocrotta' in mon.mname \
    # or 'mimic' in mon.mname
    return is_pet or mon.mname in DANGEROUS_MONSTERS


def consider_melee_only_ranged_if_hp_full(agent, monster):
    return monster[3].mname in ('brown mold', 'blue jelly') and agent.blstats.hitpoints == agent.blstats.max_hitpoints
