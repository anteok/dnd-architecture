from entities.skills import (
    StrengthSkills,
    CharismaSkills,
    DexteritySkills,
    IntelligenceSkills,
    WisdomSkills,
    ConstitutionSkills,
)


class TestSkills:

    def test_increment_all_modifiers_strength(self):
        strength_skills = StrengthSkills(4)
        assert strength_skills.athletics.modifier == 4
        assert strength_skills.saving_throw.modifier == 4

        strength_skills.increment_all_modifiers(2)
        assert strength_skills.athletics.modifier == 6
        assert strength_skills.saving_throw.modifier == 6

        strength_skills.increment_all_modifiers(-3)
        assert strength_skills.athletics.modifier == 3
        assert strength_skills.saving_throw.modifier == 3

    def test_increment_all_modifiers_dexterity(self):
        dexterity_skills = DexteritySkills(4)
        assert dexterity_skills.acrobatics.modifier == 4
        assert dexterity_skills.sleight_of_hand.modifier == 4
        assert dexterity_skills.stealth.modifier == 4
        assert dexterity_skills.saving_throw.modifier == 4

        dexterity_skills.increment_all_modifiers(2)
        assert dexterity_skills.acrobatics.modifier == 6
        assert dexterity_skills.sleight_of_hand.modifier == 6
        assert dexterity_skills.stealth.modifier == 6
        assert dexterity_skills.saving_throw.modifier == 6

        dexterity_skills.increment_all_modifiers(-3)
        assert dexterity_skills.acrobatics.modifier == 3
        assert dexterity_skills.sleight_of_hand.modifier == 3
        assert dexterity_skills.stealth.modifier == 3
        assert dexterity_skills.saving_throw.modifier == 3

    def test_increment_all_modifiers_intelligence(self):
        intelligence_skills = IntelligenceSkills(4)
        assert intelligence_skills.arcana.modifier == 4
        assert intelligence_skills.nature.modifier == 4
        assert intelligence_skills.history.modifier == 4
        assert intelligence_skills.religion.modifier == 4
        assert intelligence_skills.investigation.modifier == 4
        assert intelligence_skills.saving_throw.modifier == 4

        intelligence_skills.increment_all_modifiers(2)
        assert intelligence_skills.arcana.modifier == 6
        assert intelligence_skills.nature.modifier == 6
        assert intelligence_skills.history.modifier == 6
        assert intelligence_skills.religion.modifier == 6
        assert intelligence_skills.investigation.modifier == 6
        assert intelligence_skills.saving_throw.modifier == 6

        intelligence_skills.increment_all_modifiers(-3)
        assert intelligence_skills.arcana.modifier == 3
        assert intelligence_skills.nature.modifier == 3
        assert intelligence_skills.history.modifier == 3
        assert intelligence_skills.religion.modifier == 3
        assert intelligence_skills.investigation.modifier == 3
        assert intelligence_skills.saving_throw.modifier == 3

    def test_increment_all_modifiers_constitution(self):
        constitution_skills = ConstitutionSkills(4)
        assert constitution_skills.saving_throw.modifier == 4

        constitution_skills.increment_all_modifiers(2)
        assert constitution_skills.saving_throw.modifier == 6

        constitution_skills.increment_all_modifiers(-3)
        assert constitution_skills.saving_throw.modifier == 3

    def test_increment_all_modifiers_wisdom(self):
        wisdom_skills = WisdomSkills(4)
        assert wisdom_skills.insight.modifier == 4
        assert wisdom_skills.medicine.modifier == 4
        assert wisdom_skills.survival.modifier == 4
        assert wisdom_skills.perception.modifier == 4
        assert wisdom_skills.animal_handling.modifier == 4
        assert wisdom_skills.saving_throw.modifier == 4

        wisdom_skills.increment_all_modifiers(2)
        assert wisdom_skills.insight.modifier == 6
        assert wisdom_skills.medicine.modifier == 6
        assert wisdom_skills.survival.modifier == 6
        assert wisdom_skills.perception.modifier == 6
        assert wisdom_skills.animal_handling.modifier == 6
        assert wisdom_skills.saving_throw.modifier == 6

        wisdom_skills.increment_all_modifiers(-3)
        assert wisdom_skills.insight.modifier == 3
        assert wisdom_skills.medicine.modifier == 3
        assert wisdom_skills.survival.modifier == 3
        assert wisdom_skills.perception.modifier == 3
        assert wisdom_skills.animal_handling.modifier == 3
        assert wisdom_skills.saving_throw.modifier == 3

    def test_increment_all_modifiers_charisma(self):
        charisma_skills = CharismaSkills(4)
        assert charisma_skills.deception.modifier == 4
        assert charisma_skills.persuasion.modifier == 4
        assert charisma_skills.performance.modifier == 4
        assert charisma_skills.intimidation.modifier == 4
        assert charisma_skills.saving_throw.modifier == 4

        charisma_skills.increment_all_modifiers(2)
        assert charisma_skills.deception.modifier == 6
        assert charisma_skills.persuasion.modifier == 6
        assert charisma_skills.performance.modifier == 6
        assert charisma_skills.intimidation.modifier == 6
        assert charisma_skills.saving_throw.modifier == 6

        charisma_skills.increment_all_modifiers(-3)
        assert charisma_skills.deception.modifier == 3
        assert charisma_skills.persuasion.modifier == 3
        assert charisma_skills.performance.modifier == 3
        assert charisma_skills.intimidation.modifier == 3
        assert charisma_skills.saving_throw.modifier == 3
