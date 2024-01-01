#include <iostream>
#include "System.h"

void System::addContact(const std::string& name, const std::string& email, const std::string& phoneNumber) {
  
  contactSystem.emplace(name, Contact(name, email, phoneNumber));
  std::cout << "Contact added successfully." << std::endl;
  
}

void System::removeContact(const std::string& name) {
  
  contactSystem.erase(name);
  std::cout << "Contact removed." << std::endl;
  
}

void System::updateContact(const std::string& name, const std::string& updateEmail, const std::string& updateNumber) {
  
  auto it = contactSystem.find(name);

  if (it != contactSystem.end()) {
    
    it->second.setEmail(updateEmail);
    it->second.setPhoneNumber(updateNumber);
    std::cout << "Contact has beeen updated successfully." << std::endl;
  }
  else {
    std::cout << "Contact cannot be found" << std::endl;
  }
  
}

void System::displayContacts() const {
  
  std::cout << "Contact List:" << std::endl;
  
  for (const auto& contact : contactSystem) {
    std::cout << "Name: " << contact.second.getName() << ", Phone: " 
              << contact.second.getPhoneNumber()
              << ", Email: " << contact.second.getEmail() << std::endl;
    std::cout << std::endl;
  }
  
}
