import graphene
from graphene_django import DjangoObjectType
from .models import House, Members

#########
# TYPES #
#########
class HouseType(DjangoObjectType):
    class Meta:
        model = House

class MembersType(DjangoObjectType):
    class Meta:
        model = Members

#############
# MUTATIONS #
#############

## --> HOUSE <-- ##
class HouseCreate(graphene.Mutation):
    house = graphene.Field(HouseType)
    
    class Arguments:
        name = graphene.String(required=True)
    
    def mutate(self, info, **kwargs):
        name = kwargs.get('name')
        house = House.objects.create(name=name)

        return HouseCreate(house=house)

class HouseUpdate(graphene.Mutation):
    house = graphene.Field(HouseType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
    
    def mutate(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            house = House.objects.get(pk=id)
            house.name = name if name is not None else house.name
            house.save()

        return HouseUpdate(house=house)

class HouseDelete(graphene.Mutation):
    house = graphene.Field(HouseType)

    class Arguments:
        id = graphene.Int(required=True)
    
    def mutate(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            house = House.objects.get(pk=id)
            house.delete()

        return HouseDelete(house=None)

## --> MEMBER <-- ##
class MemberCreateMutation(graphene.Mutation):
    member = graphene.Field(MembersType)
    
    class Arguments:
        name = graphene.String(required=True)
        house_id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        #Get Arguments
        name = kwargs.get('name')
        house_id = kwargs.get('house_id')

        #Get house object and create member
        house = House.objects.get(pk=house_id)
        member = Members.objects.create(name=name, house=house)

        return MemberCreateMutation(member=member)

class MemberDeleteMutation(graphene.Mutation):
    member = graphene.Field(MembersType)

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, **kwargs):
        #Get Arguments
        id = kwargs.get('id')

        #Get member
        if id is not None:
            member = Members.objects.get(pk=id)
            member.delete()

        return MemberDeleteMutation(member=None)

class MemberUpdateMutation(graphene.Mutation):
    member = graphene.Field(MembersType)

    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    def mutate(self, info, **kwargs):
        #Get Arguments
        id = kwargs.get('id')
        name = kwargs.get('name')

        #Get member
        if id is not None:
            member = Members.objects.get(pk=id)
            member.name = name if name is not None else member.name
            member.save()

        return MemberDeleteMutation(member=member)

class Mutation:
    create_house = HouseCreate.Field()
    update_house = HouseUpdate.Field()
    delete_house = HouseDelete.Field()
    create_member = MemberCreateMutation.Field()
    update_member = MemberUpdateMutation.Field()
    delete_member = MemberDeleteMutation.Field()

###########
# QUERIES #
###########

class Query(graphene.ObjectType):
    all_houses = graphene.List(HouseType)
    house = graphene.Field(HouseType, id=graphene.Int())
    member = graphene.Field(MembersType, id=graphene.Int(), name=graphene.String())
    all_members = graphene.List(MembersType)

    def resolve_all_houses(self, info, **kwargs):
        return House.objects.all()

    def resolve_all_members(self, info, **kwargs):
        return Members.objects.all()

    def resolve_house(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return House.objects.get(pk=id)
        else:
            return None

    def resolve_member(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Members.objects.get(pk=id)
        else:
            return None