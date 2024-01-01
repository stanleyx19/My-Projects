#ifndef CONTACT_H
#define CONTACT_H

#include <string>

class Contact {
  public:

    //Constructor
    Contact(const std::string& name, const std::string& email, const std::string& phoneNumber);

    //Destructor
    ~Contact();

    //Copy Constructor
    Contact(const Contact& other);

    //Copy Assignment Operator
    Contact& operator=(const Contact& other);

    //Setters
    void setName(const std::string& userName);
    void setEmail(const std::string& userEmail);
    void setPhoneNumber(const std::string& userPhoneNumber);

    //Getters
    std::string getName() const;
    std::string getEmail() const;
    std::string getPhoneNumber() const;

  private:
    std::string name;
    std::string email;
    std::string phoneNumber;
};

#endif