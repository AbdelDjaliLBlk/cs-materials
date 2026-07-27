import 'package:flutter/material.dart';

class IngredientsOfAMealScreen extends StatelessWidget {
  final String mealName;
  const IngredientsOfAMealScreen({super.key, required this.mealName});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(mealName),
        centerTitle: true,
        actions: [
        IconButton(
          icon: const Icon(Icons.exit_to_app),
          onPressed: () {
            Navigator.pushNamedAndRemoveUntil(
              context,
              '/login',
              (route) => false,
            );
          },
        ),
        ],

        ),
      body: Center(
        child: Text("Ingredients for $mealName"),
      ),
    );
  }
}
