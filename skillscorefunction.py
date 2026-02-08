def calculate_skill(aim, strategy, reaction):

    aim_norm = aim / 100
    strategy_norm = strategy / 100
    reaction_norm = reaction / 100

    skill_score = (
        aim_norm * 0.4 +
        strategy_norm * 0.35 +
        reaction_norm * 0.25
    )

    skill_score = skill_score * 100

    return round(skill_score, 2)

result = calculate_skill(80, 70, 60)

print("overall skill score:", result)