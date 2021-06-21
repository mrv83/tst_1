from rest_framework import serializers

from .models import Entry, Statistic


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ('date', 'distance', 'duration')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if not user.groups.filter(name__in=['Manager', 'Supervisor']).exists():
            self.Meta.fields = list(self.Meta.fields)
            self.Meta.fields.append('user')

    def create(self, validated_data):
        user = self.context['request'].user
        user_from_form = validated_data.pop('user', None)
        if user.groups.filter(name__in=['Manager', 'Supervisor']).exists():
            user = user_from_form or user
        obj = Entry.objects.create(user=user, **validated_data)
        return obj


class StatisticSerializer(serializers.ModelSerializer):
    week = serializers.SerializerMethodField()
    average_speed = serializers.SerializerMethodField()

    class Meta:
        model = Statistic
        fields = ('week_number', 'week', 'amount_entries', 'total_duration', 'total_distance', 'average_speed')

    def get_week(self, obj):
        return obj.week

    def get_average_speed(self, obj):
        return '%.2f' % (float(obj.total_distance) / obj.total_duration)
