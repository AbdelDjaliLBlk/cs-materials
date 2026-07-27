import 'package:flutter/material.dart';

class MyTextField extends StatelessWidget {
  final TextEditingController TfController;
  final String TfHintText;
  final bool isObscure;
  final Icon TfIcon;
  final String ? Function (String?) TfValidator;

  const MyTextField({
    super.key,
    required this.TfController,
    required this.TfHintText,
    required this.TfValidator,
    required this.TfIcon,
    required this.isObscure ,
  });

  @override
  Widget build(BuildContext context) {
    return TextFormField(
        controller: TfController,
        validator : TfValidator,
        obscureText: isObscure,
        decoration: InputDecoration
        (
          border : OutlineInputBorder(borderRadius: BorderRadius.circular(18)),
          filled: true,
          hintText: TfHintText,
          
          hintStyle: TextStyle(color: Colors.grey[500]),
          prefixIcon: TfIcon,
        )
      );
    
  }
}