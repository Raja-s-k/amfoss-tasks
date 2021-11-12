import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.green[400],
      appBar: AppBar(
        backgroundColor: Colors.green[700],
        title: Text("WELCOME"),
      ),
      body: Container(
        child: Center(
          child: Text("              Myself Raja sk \n I am a good at programming \n                      and \n my hobbies are hearing musics \n           and doing art works"),
        ),
      ),
    );
  }
}
