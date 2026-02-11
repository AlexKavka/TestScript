from script import find_tallest_hero, Gender

class Test:

    def test_male_with_job(self):
        result = find_tallest_hero(Gender.MALE, True)

        assert result
        assert 'name' in result
        assert 'appearance' in result
        assert 'work' in result
        assert result['appearance']['gender'] == 'Male'
        assert result['work']['occupation'] != '-'

    def test_male_no_job(self):
        result = find_tallest_hero(Gender.MALE, False)

        assert result
        assert 'name' in result
        assert 'appearance' in result
        assert 'work' in result
        assert result['appearance']['gender'] == 'Male'
        assert result['work']['occupation'] == '-'

    def test_female_no_job(self):
        result = find_tallest_hero(Gender.FEMALE, False)

        assert result
        assert result['appearance']['gender'] == 'Female'
        assert result['work']['occupation'] == '-'

    def test_female_with_job(self):
        result = find_tallest_hero(Gender.FEMALE, True)

        assert result
        assert result['appearance']['gender'] == 'Female'
        assert result['work']['occupation'] != '-'

    def test_height_conversion(self):
        result = find_tallest_hero(Gender.MALE, True)

        if result:
            height = result['appearance']['height']
            assert height[0] != "-" or height[1] != "-"

    def test_multiple_calls(self):
        result1 = find_tallest_hero(Gender.MALE, True)
        result2 = find_tallest_hero(Gender.MALE, True)

        assert result1['id'] == result2['id']


if __name__ == "__main__":
    Test