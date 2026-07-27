import 'package:flutter_application_1/models/meal.dart';
import 'package:hive/hive.dart'; 
part 'meals_of_a_day.g.dart';

@HiveType(typeId: 1) 
class MealsOfADay extends HiveObject{
  @HiveField(0) 
  final String day;
  @HiveField(1)
  final List<Meal> listOfMealsOfDay;

  MealsOfADay({
   required this.day,
   required this.listOfMealsOfDay,
  });
}
