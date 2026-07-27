import 'package:flutter/material.dart';

class MealCard extends StatelessWidget {
  final String mealName;
  final String imagePath;
  final VoidCallback onDelete; 
  final BuildContext parentContext;

  const MealCard({
    required this.mealName,
    required this.imagePath,
    required this.onDelete,
    required this.parentContext,
    super.key,
  });

  @override
  Widget build(BuildContext context) {

    return Card(
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      elevation: 2,
      color: Colors.orange,
      margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Row(
          children: [

            Container(
              width: 78,
              height: 78,
              decoration: BoxDecoration(
                color: Colors.orange,
                borderRadius: BorderRadius.circular(6),
              ),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(6),
                child: Image.asset(
                  imagePath,
                  width: 78,
                  height: 78,
                  fit: BoxFit.cover,
                ),
              ),
            ),
            SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    mealName,
                    style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 6),
                ],
              ),
            ),

            Column(
              mainAxisSize: MainAxisSize.min,
              children: [

                IconButton(
                  icon: const Icon(Icons.remove_red_eye),
                  color: Colors.black,
                  onPressed: () {
                  Navigator.pushNamed(
                    parentContext,
                    '/ingredients',
                    arguments: mealName,
                  );
                },

                ),

                IconButton(
                  icon: const Icon(Icons.delete),
                  color: Colors.black,
                  onPressed: (){},
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
