import 'package:flutter/material.dart';

class MyTextButton extends StatelessWidget {
  final String buttonLabel;
  final Function() onPressedFct;

  const MyTextButton({super.key, required this.buttonLabel, required this.onPressedFct});
  @override
  Widget build(BuildContext context){
    return TextButton(
      onPressed: onPressedFct,
      child: Text(
        buttonLabel,
        style: const TextStyle(
          fontSize: 16,
          fontWeight: FontWeight.bold,
          color: Colors.blue
        ),
      ),
    );   
  }
}    
  
class MyElevatedButton extends StatelessWidget {
  final String buttonLabel;
  final Function() onPressedFct;

  const MyElevatedButton({super.key, required this.buttonLabel, required this.onPressedFct});
  @override
  Widget build(BuildContext context){
    return ElevatedButton(
      onPressed: onPressedFct,
      style: ElevatedButton.styleFrom(
        backgroundColor: const Color.fromARGB(255, 109, 97, 97),
      ),
      child: Text(
        buttonLabel,
        style: const TextStyle(
          fontSize: 16,
          fontWeight: FontWeight.bold,
          color: Color.fromARGB(255, 253, 155, 7),
        ),
      ),
    );   
  }
}
