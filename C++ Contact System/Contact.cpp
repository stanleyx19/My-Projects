#include "Contact.h"

//Constructor 
Contact::Contact(const std::string& name, const std::string& email, const std::string& phoneNumber) {
  
  this->name = name;
  this->email = email;
  this->phoneNumber = phoneNumber;
  
}

//Copy Constructor
Contact::Contact(const Contact& other) {
  
  this->name = other.name;
  this->email = other.email;
  this->phoneNumber = other.phoneNumber;
  
}

//Copy Assignment Operator
Contact& Contact::operator=(const Contact& other) {

  if (this != &other) {

    name.clear();
    email.clear();
    phoneNumber.clear();
    
    this->name = other.name;
    this->email = other.email;
    this->phoneNumber = other.phoneNumber;
  }
  return *this;
  
}

//Setters
void Contact::setName(const std::string& userName) {
  this->name = userName;
}

void Contact::setEmail(const std::string& userEmail) {
  this->email = userEmail;
}

void Contact::setPhoneNumber(const std::string& userPhoneNumber) {
  this->phoneNumber = userPhoneNumber;
}

//Getters
std::string Contact::getName() const {
  return this->name;
}

std::string Contact::getEmail() const {
  return this->email;
}

std::string Contact::getPhoneNumber() const {
  return this->phoneNumber;
}