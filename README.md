# LiftMovementSimulator
Function will return a list of floors that the lift has stopped at.

**Lift Rules (Knuth's Elevator algorithm)** :  
  -  Proceed in the same direction until the last request in that direction.
  -  If there is no request, stop and proceed towards other direction, if there is any request                                                  from other direction.
                                        
**People Rules** : 
  - People are in "queues" that represent their order of arrival to wait for the Lift.
  - All people can press the UP/DOWN Lift-call buttons.
  - Only people going the same direction as the Lift may enter it.
  - If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call button again after it has left                           without them.

**Example input** :
  - queues= ( (),   (0,),  (),      (),   (2,),  (3,),  () )
  - capacity >= 1
  - 0 is ground floor.
  - capacity represents the maximum no of people in a lift.


**Assumptions** : 
  - People will not go to floors that does not exist.
  - Lift will always start at ground floor.
  - People will not go to floors that they are already on.
  - There's no basement.
