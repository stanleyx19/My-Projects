#include "System.h"
#include <iostream>

void viewMenu(System& contactSystem) {
  
  std::cout << "Welcome to the Contact Management System!" << std::endl;
  std::cout << "Please select an option:" << std::endl;
  std::cout << std::endl;

  while (true) {
    
    std::cout << "1. Add Contact" << std::endl;
    std::cout << "2. Remove Contact" << std::endl;
    std::cout << "3. Update Contact" << std::endl;
    std::cout << "4. Display Contacts" << std::endl;
    std::cout << "5. Quit" << std::endl;
    std::cout << std::endl;
    std::cout << "Enter your choice: " << std::endl;

    int choice;
    std::cin >> choice;

    if (std::cin.fail()) {
      throw std::runtime_error("Invalid input.");
    }
    
    std::cout << std::endl;

    if (choice == 1) {
      
      std::string name;
      std::string phone;
      std::string email;
      
      std::cout << "Enter the name of the contact: ";
      std::cin >> name;
      
      std::cout << "Enter the phone number of the contact: ";
      std::cin >> phone;
      
      std::cout << "Enter the email address of the contact: ";
      std::cin >> email;
      
      contactSystem.addContact(name, phone, email);
      std::cout << std::endl;
      
    }
      
    else if (choice == 2) {
      
      std::string name;
      
      std::cout << "Enter the name of the contact to remove: ";
      std::cin >> name;
      
      contactSystem.removeContact(name);
      std::cout << std::endl;
      
    }
      
    else if (choice == 3) {
      
      std::string name;
      std::string email;
      std::string phone;

      std::cout << "Enter the name of the contact to update: ";
      std::cin >> name;
      
      std::cout << "Enter the new email address: ";
      std::cin >> email;
      
      std::cout << "Enter the new phone number: ";
      std::cin >> phone;

      contactSystem.updateContact(name, email, phone);
      std::cout << std::endl;
      
    }
    else if (choice == 4) {
      
      contactSystem.displayContacts();
      
    }
      
    else if (choice == 5) {
      
      std::cout << "Thank you for using the Contact Management System!" << std::endl;
      break;
      
    }
      
    else {
      
      std::cout << "Invalid Choice. Please enter a valid choice." << std::endl;
      std::cout << std::endl;
      
    }
    
  }
  
}


int main() {
  
  System contactSystem;
  
  viewMenu(contactSystem);
  
  return 0;
}