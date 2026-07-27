import 'package:flutter/material.dart' ;
import 'package:flutter_application_1/models/meals_of_a_day.dart';

class WeekDaysCard extends StatelessWidget {
  final MealsOfADay dayAndItsMealsList;
  const WeekDaysCard({
    super.key,
     required this.dayAndItsMealsList,
    });
  
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 80,
      width: 145,
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        border: Border.all(color: Colors.black),
        color: Colors.amber,
        borderRadius: BorderRadius.all(
          Radius.circular(10),
        ),
      ),
      child: Column(
        children: [
          Expanded(
            child: Align(
              alignment: Alignment.centerLeft,
              child: Text(
                dayAndItsMealsList.day,
                style: const TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
          const SizedBox(height: 5),
          Expanded(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                IconButton(
                  icon: const Icon(Icons.visibility),
                  color: Colors.orange,
                  onPressed: () {
                    Navigator.pushNamed(
                    context,
                    '/mealsOfADay',
                    arguments: dayAndItsMealsList,
                  );
                },
                ),
                const SizedBox(width: 20),
                IconButton(
                  icon: const Icon(Icons.add),
                  color: Colors.black,
                  onPressed: () {
                  Navigator.pushNamedAndRemoveUntil(
                    context,
                    '/addMeal',
                    (route) => false,
                  );
                },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
