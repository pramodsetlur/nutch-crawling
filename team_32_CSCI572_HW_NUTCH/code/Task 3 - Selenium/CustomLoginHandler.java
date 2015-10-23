package org.apache.nutch.protocol.interactiveselenium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.By;

public class CustomHandlerLogin implements InteractiveSeleniumHandler {


    public void processDriver(WebDriver driver) {

        String OriginalURL = driver.getCurrentUrl();
        driver.get(OriginalURL);

        //Find the login button and click on it
        WebElement LoginButton = driver.findElement(By.linkText("Login"));
        LoginButton.click();

        //Find the username textbox using the name of the textbox - which is typically "Username"
        WebElement useremail = driver.findElement(By.linkText("Username"));

        //if username is not found try finding an element with "email"
        if (null == useremail) {
            useremail = driver.findElement(By.linkText("email"));
        }
        useremail.clear();
        useremail.sendKeys("cs572team32@gmail.com");

        WebElement password = driver.findElement(By.linkText("Password"));
        password.clear();
        password.sendKeys("ViewSonic");

        WebElement submitButton = driver.findElement(By.linkText("submit"));
        submitButton.click();
    }

    public boolean shouldProcessURL(String URL) {
        return true;
    }
}