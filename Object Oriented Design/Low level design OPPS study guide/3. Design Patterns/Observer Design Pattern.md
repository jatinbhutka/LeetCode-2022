# Observer Design Pattern:

Use Case: When something like DB changes, You have to do or notify many subsequence of process. how does that happens?

- Suppose you logged in application to multiple devices eg. Email, slack, gmail, using phone, diff laptop, IPad, as msg/mail comes, all of this devices has to be notified. How does that happens?

-  Group msg notification, How can all the people can be notify for msg?



- There is publisher, who publish the change
- There is a subscriber who will be notify for the changes. (Subscriber can be opt as Unsubscribe as well)


- Subject:
- Observer: of the subject who will be notify for any change in the subject.


<img width="1486" alt="image" src="https://user-images.githubusercontent.com/35987583/182095925-9f6d35e1-84d7-47e0-b8f2-b40f2a01d745.png">
