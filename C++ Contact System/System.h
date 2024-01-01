#ifndef SYSTEM_H
#define SYSTEM_H

#include "Contact.h"
#include <unordered_map>

class System {
  public:

    void addContact(const std::string& name, const std::string& email, const std::string& phoneNumber);

    void removeContact(const std::string& name);

    void updateContact(const std::string& name, const std::string& updateEmail, const std::string& updateNumber); 

    void displayContacts() const;

  private:
    std::unordered_map<std::string, Contact> contactSystem; //Hashmap
  
};

#endif