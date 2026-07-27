import 'package:flutter/material.dart';
import 'package:flutter_application_1/components/my_buttons.dart';
import 'package:flutter_application_1/components/my_textfield.dart';
import 'package:flutter_application_1/screens/signup_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController userController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  @override
  void dispose() {
    userController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(36.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              "Welcome to Meal Planner",
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold,color: Colors.blueGrey),
            ),
            const SizedBox(height: 20),
            const CircleAvatar(
              backgroundImage: AssetImage("assets/images/user.png"),
              radius: 60,
            ),
            const SizedBox(height: 40),
            MyTextField(
              TfController: userController,
  
              TfHintText: "Email",
              isObscure: false,
              TfIcon: const Icon(Icons.email),
              TfValidator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter your email';
                }
                return null;
              },
            ),
            const SizedBox(height: 30),
            MyTextField(
              TfController: passwordController,
              TfHintText: "Password",
              isObscure: true,
              TfIcon: const Icon(Icons.lock),
              TfValidator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter your password';
                }
                return null;
              },
            ),
            const SizedBox(height: 20),
            MyElevatedButton(
              buttonLabel: "Login",
              onPressedFct: () {
                //print("Email: ${userController.text}");
                //print("Password: ${passwordController.text}");
              },
            ),
            const SizedBox(height: 30),
            MyTextButton(
              buttonLabel: "Forgot Password",
              onPressedFct: () {},
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Don't have an account?"),
                MyTextButton(
                  buttonLabel: "Sign Up",
                  onPressedFct: () {
                    Navigator.push(context, MaterialPageRoute(builder: (context) =>  SignupScreen()));
                  },
                ),
              ],
            ),
          ],
        ),
      ),
      
    );
  }
}
