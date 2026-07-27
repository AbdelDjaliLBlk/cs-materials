import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:flutter_application_1/models/meal.dart';
import 'package:flutter_application_1/models/meals_of_a_day.dart';
class AddNewMealScreen extends StatefulWidget {
  const AddNewMealScreen({super.key});

  @override
  _AddNewMealScreenState createState() => _AddNewMealScreenState();
}

class _AddNewMealScreenState extends State<AddNewMealScreen> {
  final meal = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Add Meal")),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            TextField(
              controller: meal,
              decoration: InputDecoration(
                hintText: "Meal name",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () async{
                final dayMealsBox = await Hive.openBox<MealsOfADay>('MealsBDD'); 
                //dayMealsBox.put(); 
                //Meal newMeal = Meal();
                Navigator.pop(context, newMeal);
              },
              child: Text("Add"),
            )
          ],
        ),
      ),
    );
  }
}
