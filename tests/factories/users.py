import factory
import faker
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Faker('email')
    nickname = factory.LazyAttribute(lambda obj: faker.Faker().first_name()[:10])
    password = factory.Faker('password')