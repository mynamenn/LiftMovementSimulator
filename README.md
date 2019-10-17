# LiftMovementSimulator
Function will return a list of floors that the lift has stopped at.

**Lift Rules (Knuth's Elevator algorithm)** :  1. Proceed in the same direction until the last request in that direction.
                                          2. If there is no request, stop and proceed towards other direction, if there is any request                                                  from other direction.
                                        
**People Rules** : 1. People are in "queues" that represent their order of arrival to wait for the Lift.
               2. All people can press the UP/DOWN Lift-call buttons.
               3. Only people going the same direction as the Lift may enter it.
               4. If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call button again after it has left                           without them.

**Example input** : queues= ( (),   (0,),  (),      (),   (2,),  (3,),  () )
               capacity >= 1
               *0 is ground floor.
               *capacity represents the maximum no of people in a lift.


**Assumptions** : 1. People will not go to floors that does not exist.
              2. Lift will always start at ground floor.
              3. People will not go to floors that they are already on.
              4. There's no basement.
