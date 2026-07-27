import 'package:flutter/material.dart';
import 'package:flutter_application_1/components/my_buttons.dart';
import 'package:flutter_application_1/components/my_textfield.dart';
import 'package:flutter_application_1/screens/login_screen.dart';
class SignupScreen extends StatefulWidget{
  const SignupScreen({super.key});

  @override
  _SignupScreenState createState() => _SignupScreenState();
}

class _SignupScreenState extends State<SignupScreen> {
  final TextEditingController userController = TextEditingController();
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  @override
  void dispose() {
    userController.dispose();
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Container(
            padding: EdgeInsets.all(36.0),
          child: Column(
            children: [
              const SizedBox(height: 20),
              Text("Create Your Account",style: TextStyle(
                fontSize: 20,
                color : const Color.fromARGB(255, 0, 37, 56),
                fontWeight: FontWeight.bold
              ),),
              const SizedBox(height: 50),
              MyTextField(TfController: userController ,isObscure: false ,TfIcon:Icon(Icons.person), TfHintText: "Username", TfValidator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter your username';
                }
                return null;
              },),
              const SizedBox(height: 20),
              MyTextField(TfController: emailController ,TfIcon:Icon(Icons.email),isObscure: false, TfHintText: "Email", TfValidator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter your email';
                }
                return null;
              },),
              const SizedBox(height: 20),
              MyTextField(TfController: passwordController ,TfIcon:Icon(Icons.lock),isObscure: true, TfHintText: "Password", TfValidator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter your password';
                }
                return null;
              },),
              const SizedBox(height: 20),
              MyTextField(TfController: passwordController,isObscure: true, TfHintText: "Confirm Password",TfIcon: Icon(Icons.lock),TfValidator: (value) {
                 if (value == null || value.isEmpty) {
                  return 'Please confirm your password';
                }
                 return null;
              },),
              const SizedBox(height: 20),
              MyElevatedButton(buttonLabel: "Sign Up", onPressedFct: (){},),
              const SizedBox(height: 10),
              Text("OR",style: TextStyle(
                fontSize: 13,
                color : Colors.blueGrey,
              ),),
              const SizedBox(height: 10),
              MyElevatedButton(buttonLabel: "Sign with Google", onPressedFct: (){},),
              const SizedBox(height: 20),
              Row(mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text("Already have an account?",style: TextStyle(
                  fontSize: 13,
                color : Colors.blueGrey,
                ),),
                MyTextButton(
                  buttonLabel: "Login",
                  onPressedFct: () {
                    Navigator.push(context, MaterialPageRoute(builder: (context) =>  LoginScreen()));
                  },
                ),
              ],),
            ],
          ),
        ),
      ),
    );
  }


}