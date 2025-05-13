'''This is the dictionary of all moves for each category and a blitz mode dictionary that contains roughly all moves regardless of category. Can be modified when new moves are added.'''

moves = {
    # OFFENSE
    1: 
        {1: {1: {1: {1:
                    ['Left hand inside knee pull, single leg entry to take down', 
                    'Attempted arm drag, to left hand inside achilles grab, single leg take down',
                    'Sit criss-cross, double outside knee pull up to bear-hug legs mid-thigh, head outside, hips up back straight, pull opponent\'s legs out to right side take down',
                    'Scoot under into right leg straight footlock position, finish sweep'],  # Seated guard, standing opp, right side, takedowns
                    2: 
                    ['Left hand inside knee pull, invert under legs, finish knee bar',
                    'Scoot under into right leg straight footlock position, sweep to footlock finish']    # Seated guard, standing opp, right side, leg locks
                    },
                2: {1:
                    ['Right hand inside knee pull, single leg entry to take down', 
                    'Attempted arm drag, to right hand inside achilles grab, single leg take down',
                    'Sit criss-cross, double outside knee pull up to bear-hug legs mid-thigh, head outside, hips up back straight, pull opponent\'s legs out to left side take down'
                    'Scoot under into left leg straight footlock position, finish sweep'],  # Seated guard, standing opp, left side, takedowns
                    2: 
                    ['Right hand inside knee pull, invert under legs, finish knee bar',
                    'Scoot under into left leg straight footlock position, sweep to footlock finish']    # Seated guard, standing opp, left side, leg locks
                    },
                3: {1:
                    ['Right hand inside knee pull, single leg entry to take down', 
                    'Attempted arm drag, to right hand inside achilles grab, single leg take down',
                    'Left hand inside knee pull, single leg entry to take down', 
                    'Attempted arm drag, to left hand inside achilles grab, single leg take down',
                    'Sit criss-cross, double outside knee pull up to bear-hug legs mid-thigh, head outside, hips up back straight, pull opponent\'s legs out to right side take down',
                    'Sit criss-cross, double outside knee pull up to bear-hug legs mid-thigh, head outside, hips up back straight, pull opponent\'s legs out to left side take down'],   # Seated guard, standing opp, both sides, takedowns
                    2: 
                    ['Right hand inside knee pull, invert under legs, finish knee bar', 
                    'Scoot under into right leg straight footlock position, sweep to footlock finish',
                    'Left hand inside knee pull, invert under legs, finish knee bar', 
                    'Scoot under into left leg straight footlock position, sweep to footlock finish']    # Seated guard, standing opp, both sides, leg locks
                    }
                },
            2: {1: {1:
                    ['Post right hand against same-side shoulder, hop out to right side with right leg between opponent, invert under legs, roll through finish knee bar',
                    'Post right hand against same-side shoulder, hop out to right side with right leg between opponent, invert under legs, roll back into opponents\'s legs, finish knee bar']  # Seated guard, kneeling opp, right side, leg locks
                    },
                2: {1:
                    ['Post left hand against same-side shoulder, hop out to left side with left leg between opponent, invert under legs, roll through finish knee bar',
                    'Post left hand against same-side shoulder, hop out to left side with left leg between opponent, invert under legs, roll back into opponents\'s legs, finish knee bar'] # Seated guard, kneeling opp, left side, leg locks
                    },
                3: {1:
                    ['Post right hand against same-side shoulder, hop out to right side with right leg between opponent, invert under legs, roll through finish knee bar',
                    'Post right hand against same-side shoulder, hop out to right side with right leg between opponent, invert under legs, roll back into opponents\'s legs, finish knee bar',
                    'Post left hand against same-side shoulder, hop out to left side with left leg between opponent, invert under legs, roll through finish knee bar',
                    'Post left hand against same-side shoulder, hop out to left side with left leg between opponent, invert under legs, roll back into opponents\'s legs, finish knee bar'] # Seated guard, kneeling opp, both sides, leg locks
                    }
                }
            }, 
        2: {1: {1: {1: 
                    ['Left leg reverse butterfly hook, early leg entry option, finish knee bar', 
                    'Left leg reverse butterfly hook, full sweep leg entry option, finish knee bar'],    # Reverse Z-Guard, opp body lock, right side, leg locks
                    },
                2: {1:
                    ['Right leg reverse butterfly hook, early leg entry option, finish knee bar', 
                    'Right leg reverse butterfly hook, full sweep leg entry option, finish knee bar'],  # Reverse Z-Guard, opp body lock, left side, leg locks
                    },
                3: {1:
                    ['Left leg reverse butterfly hook, early leg entry option, finish knee bar', 
                    'Left leg reverse butterfly hook, full sweep leg entry option, finish knee bar',
                    'Right leg reverse butterfly hook, early leg entry option, finish knee bar', 
                    'Right leg reverse butterfly hook, full sweep leg entry option, finish knee bar'],  # Reverse Z-Guard, opp body lock, both sides, leg locks
                    }
                },
            2: {1: {1: 
                    ['Left leg reverse butterfly hook, opponent\'s left arm reaches over your shoulder, right hand far trap grip, left hand chin-strap, roll over sweep to left']   # Reverse Z-Guard, opp arm over shoulder, right side, sweeps            
                    },
                2: {1:
                    ['Right leg reverse butterfly hook, opponent\'s right arm reaches over your shoulder, left hand far trap grip, right hand chin-strap, roll over sweep to right']    # Reverse Z-Guard, opp arm over shoulder, left side, sweeps
                    },
                3: {1:
                    ['Left leg reverse butterfly hook, opponent\'s left arm reaches over your shoulder, right hand far trap grip, left hand chin-strap, roll over sweep to left',
                    'Right leg reverse butterfly hook, opponent\'s right arm reaches over your shoulder, left hand far trap grip, right hand chin-strap, roll over sweep to right']     # Reverse Z-Guard, opp arm over shoulder, both sides, sweeps
                    }
                }
            },
        3: {1: {1: {1:
                    ['Left leg between opponent\'s legs, angle upper-body towards opponent\'s far hip, knee lever sweep',
                    'Left leg between opponent\'s legs under their left shin, right leg wrapped over top opponent\'s leg, opponent\'s knee is past bottom thigh, secure right hand under hook to far side ribs and left hand grip behind opponent\'s right knee, opponent secures whizzer, begin to walk hips under opponent using left foot, once under opponent continue sweeping motion to the right'], # Half guard bottom, opp inside knee down, right side, sweeps
                    2: 
                    ['Left leg between opponent\'s legs under their left shin, right leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure right hand under hook to far side ribs, opponent secures whizzer, attempt to roll under and secure deep half guard, opponent reacts basing out both hands, leading with your head come around to the under hook side and press left ear to opponent\'s lower back left side, get as much height as possible coming up to right knee between opponent\'s legs and left leg based out with rear body lock, take the back',
                    'Left leg between opponent\'s legs under their left shin, right leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure right hand under hook to far side ribs, opponent secures heavy whizzer, replace under hook to arm wrap grip behind opponent\'s left thigh, begin to come up into the dog fight position, secure waist grip again and transition it to push into opponent\'s left side of face, bring hips up and hop around to far side of opponent\'s body, take the back',
                    'Left leg between opponent\'s legs under their left shin, right leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure right hand under hook to far side ribs, opponent secures heavy whizzer, replace under hook to arm wrap grip behind opponent\'s left thigh, begin to come up into the dog fight position, secure waist grip again, opponent is pressing heavy with the whizzer, limp arm out and secure body lock, take the back']   # Half guard bottom, opp inside knee down, right side, back takes
                    },
                2: {1: 
                    ['Right leg between opponent\'s legs, angle upper-body towards opponent\'s far hip, knee lever sweep'], # Half guard bottom, opp inside knee down, left side, sweeps
                    2:
                    ['Right leg between opponent\'s legs under their right shin, left leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure left hand under hook to far side ribs, opponent secures whizzer, attempt to roll under and secure deep half guard, opponent reacts basing out both hands, leading with your head come around to the under hook side and press right ear to opponent\'s lower back right side, get as much height as possible coming up to left knee between opponent\'s legs and right leg based out with rear body lock, take the back',
                    'Right leg between opponent\'s legs under their right shin, left leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure left hand under hook to far side ribs, opponent secures heavy whizzer, replace under hook to arm wrap grip behind opponent\'s right thigh, begin to come up into the dog fight position, secure waist grip again and transition it to push into opponent\'s right side of face, bring hips up and hop around to far side of opponent\'s body, take the back',
                    'Right leg between opponent\'s legs under their right shin, left leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure left hand under hook to far side ribs, opponent secures heavy whizzer, replace under hook to arm wrap grip behind opponent\'s right thigh, begin to come up into the dog fight position, secure waist grip again, opponent is pressing heavy with the whizzer, limp arm out and secure body lock, take the back']   # Half guard bottom, opp inside knee down, left side, back takes
                    },
                3: {1: 
                    ['Left leg between opponent\'s legs, angle upper-body towards opponent\'s far hip, knee lever sweep',
                    'Right leg between opponent\'s legs, angle upper-body towards opponent\'s far hip, knee lever sweep'],   # Half guard bottom, opp inside knee down, both sides, sweeps
                    2:
                    ['Right leg between opponent\'s legs under their right shin, left leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure left hand under hook to far side ribs, opponent secures whizzer, attempt to roll under and secure deep half guard, opponent reacts basing out both hands, leading with your head come around to the under hook side and press right ear to opponent\'s lower back right side, get as much height as possible coming up to left knee between opponent\'s legs and right leg based out with rear body lock, take the back',
                    'Right leg between opponent\'s legs under their right shin, left leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure left hand under hook to far side ribs, opponent secures heavy whizzer, replace under hook to arm wrap grip behind opponent\'s right thigh, begin to come up into the dog fight position, secure waist grip again and transition it to push into opponent\'s right side of face, bring hips up and hop around to far side of opponent\'s body, take the back',
                    'Right leg between opponent\'s legs under their right shin, left leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure left hand under hook to far side ribs, opponent secures heavy whizzer, replace under hook to arm wrap grip behind opponent\'s right thigh, begin to come up into the dog fight position, secure waist grip again, opponent is pressing heavy with the whizzer, limp arm out and secure body lock, take the back',
                    'Left leg between opponent\'s legs under their left shin, right leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure right hand under hook to far side ribs, opponent secures whizzer, attempt to roll under and secure deep half guard, opponent reacts basing out both hands, leading with your head come around to the under hook side and press left ear to opponent\'s lower back left side, get as much height as possible coming up to right knee between opponent\'s legs and left leg based out with rear body lock, take the back',
                    'Left leg between opponent\'s legs under their left shin, right leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure right hand under hook to far side ribs, opponent secures heavy whizzer, replace under hook to arm wrap grip behind opponent\'s left thigh, begin to come up into the dog fight position, secure waist grip again and transition it to push into opponent\'s left side of face, bring hips up and hop around to far side of opponent\'s body, take the back',
                    'Left leg between opponent\'s legs under their left shin, right leg wrapped over top of opponent\'s leg, opponent\'s knee is past bottom thigh, secure right hand under hook to far side ribs, opponent secures heavy whizzer, replace under hook to arm wrap grip behind opponent\'s left thigh, begin to come up into the dog fight position, secure waist grip again, opponent is pressing heavy with the whizzer, limp arm out and secure body lock, take the back']   # Half guard bottom, opp inside knee down, both sides, back takes
                    }
                },
            2: {1: {1: 
                    ['Left leg between opponent\'s legs, left foot behind opponent\'s achilles pushing, establish right leg butterfly hook, with both hands under crossface armpit kick and push to extend away, finish knee bar'],  # Half guard bottom, opp inside knee up, right side, leg locks
                    2: 
                    ['Left leg between opponent\'s legs, left foot behind opponent\'s achilles pushing, establish right leg butterfly hook, with both hands under crossface armpit kick and push to extend away, secure legs to take down']  # Half guard bottom, opp inside knee up, right side, takedown
                    },
                2: {1:
                    ['Right leg between opponent\'s legs, right foot behind opponent\'s achilles pushing, establish left leg butterfly hook, with both hands under crossface armpit kick and push to extend away, finish knee bar'], # Half guard bottom, opp inside knee up, left side, leg locks
                    2:
                    ['Right leg between opponent\'s legs, right foot behind opponent\'s achilles pushing, establish left leg butterfly hook, with both hands under crossface armpit kick and push to extend away, secure legs to take down'] # Half guard bottom, opp inside knee up, left side, takedown
                    },
                3: {1:
                    ['Left leg between opponent\'s legs, left foot behind opponent\'s achilles pushing, establish right leg butterfly hook, with both hands under crossface armpit kick and push to extend away, finish knee bar',
                    'Right leg between opponent\'s legs, right foot behind opponent\'s achilles pushing, establish left leg butterfly hook, with both hands under crossface armpit kick and push to extend away, finish knee bar'], # Half guard bottom, opp inside knee up, both sides, leg locks
                    2:
                    ['Left leg between opponent\'s legs, left foot behind opponent\'s achilles pushing, establish right leg butterfly hook, with both hands under crossface armpit kick and push to extend away, secure legs to take down',
                    'Right leg between opponent\'s legs, right foot behind opponent\'s achilles pushing, establish left leg butterfly hook, with both hands under crossface armpit kick and push to extend away, secure legs to take down']  # Half guard bottom, opp inside knee up, both sides, takedown
                    }
                }
            },
        4: {1: {1: {1: 
                    ['Right leg between opponent\'s legs, backstep to knee bar finish',
                    'Right leg between opponent\'s legs, backstep to secure knee bar position, finish far leg footlock',
                    'Left leg between opponent\'s legs, secure right-side leg, sit down into straight footlock position, finish option 1',
                    'Left leg between opponent\'s legs, secure right-side leg, sit down into straight footlock position, sit up into option 2 finish',
                    'Left leg between opponent\'s legs, secure right-side leg, sit down into straight footlock position, finish option 3',
                    'Left leg between opponent\'s legs, secure right-side leg, sit down into straight footlock position, slide inside knee across, turn to knee bar finish',
                    'Right leg between opponent\'s legs, backstep to enter saddle, opponent reacts by bringing knee to chest, sit on that leg pinning to ground, apply weight from right shoulder into far side knee, step on pinned leg with left foot, left hand replaces shoulder post, lift up and hop over far leg to secure and finish knee bar']    # Standing position, supine opp, right side, leg locks
                    },
                2: {1: 
                    ['Left leg between opponent\'s legs, backstep to knee bar finish',
                    'Left leg between opponent\'s legs, backstep to secure knee bar position, finish far leg footlock',
                    'Right leg between opponent\'s legs, secure left-side leg, sit down into straight footlock position, finish option 1',
                    'Right leg between opponent\'s legs, secure left-side leg, sit down into straight footlock position, sit up into option 2 finish',
                    'Right leg between opponent\'s legs, secure left-side leg, sit down into straight footlock position, finish option 3',
                    'Right leg between opponent\'s legs, secure left-side leg, sit down into straight footlock position, slide inside knee across, turn to knee bar finish',
                    'Left leg between opponent\'s legs, backstep to enter saddle, opponent reacts by bringing knee to chest, sit on that leg pinning to ground, apply weight from left shoulder into far side knee, step on pinned leg with right foot, right hand replaces shoulder post, lift up and hop over far leg to secure and finish knee bar']    # Standing position, supine opp, left side, leg locks
                    },
                3: {1: 
                    ['Right leg between opponent\'s legs, backstep to knee bar finish',
                    'Right leg between opponent\'s legs, backstep to secure knee bar position, finish far leg footlock',
                    'Left leg between opponent\'s legs, secure right-side leg, sit down into straight footlock position, finish option 1',
                    'Left leg between opponent\'s legs, secure right-side leg, sit down into straight footlock position, sit up into option 2 finish',
                    'Left leg between opponent\'s legs, secure right-side leg, sit down into straight footlock position, finish option 3',
                    'Left leg between opponent\'s legs, secure right-side leg, sit down into straight footlock position, slide inside knee across, turn to knee bar finish',
                    'Left leg between opponent\'s legs, backstep to knee bar finish',
                    'Left leg between opponent\'s legs, backstep to secure knee bar position, finish far leg footlock',
                    'Right leg between opponent\'s legs, secure left-side leg, sit down into straight footlock position, finish option 1',
                    'Right leg between opponent\'s legs, secure left-side leg, sit down into straight footlock position, sit up into option 2 finish',
                    'Right leg between opponent\'s legs, secure left-side leg, sit down into straight footlock position, finish option 3',
                    'Right leg between opponent\'s legs, secure left-side leg, sit down into straight footlock position, slide inside knee across, turn to knee bar finish',
                    'Right leg between opponent\'s legs, backstep to enter saddle, opponent reacts by bringing knee to chest, sit on that leg pinning to ground, apply weight from right shoulder into far side leg, step on pinned leg with left foot, left hand replaces shoulder post, lift up and hop over far leg to secure and finish knee bar',
                    'Left leg between opponent\'s legs, backstep to enter saddle, opponent reacts by bringing knee to chest, sit on that leg pinning to ground, apply weight from left shoulder into far side knee, step on pinned leg with right foot, right hand replaces shoulder post, lift up and hop over far leg to secure and finish knee bar']    # Standing position, supine opp, both sides, leg locks
                    }
                },
            2: {1: {1: 
                    ['Establish left hand collar tie and elbow grip, clear elbow grip up, change levels to single leg, finish take down',
                    'Establish left hand collar tie and elbow grip, push opponent\'s head over right-side leg, finish foot-sweep take down',
                    'Opponent has body lock with head inside, establish left hand wizar on opponent\'s right arm and right hand grip on far side elbow, circle around towards opponent\'s left leg while heavy on the wizar, hop right leg in line with opponent\'s toes, left leg kicks into opponent\'s left leg at the knee, use momentum and torque to finish throw'
                    'Opponent has body lock with head outside, establish left hand airmpit grip on opponent\'s right arm and right hand grip on far side elbow, circle around towards opponent\'s left leg while heavy on the head, hop right leg in line with opponent\'s toes, left leg kicks into opponent\'s left leg at the knee, use momentum and torque to finish throw',
                    'Establish left hand wizar on opponent\'s right arm, right foot replaces left, left foot kicks the inside of opponent\'s near leg, post right hand on ground and hop into opponent while raising left leg elevating hip, finish take down'],    # Standing position, standing opp, right side, takedowns
                    2:
                    ['While four-pointed with hands and feet and opponent left side body lock, angle towards opponent\'s left leg, drop low and slide through legs on right-side outer-thigh, safely grab elbow-deep grip behind opponent\'s left knee while sliding under legs, establish saddle on the left leg and finish knee bar.']   # Standing position, standing opp, right side, leg locks
                    },
                2: {1:
                    ['Establish right hand collar tie and elbow grip, clear elbow grip up, change levels to single leg, finish take down',
                    'Establish right hand collar tie and elbow grip, push opponent\'s head over left-side leg, finish foot-sweep take down',
                    'Opponent has body lock with head inside, establish right hand wizar on opponent\'s left arm and left hand grip on far side elbow, circle around towards opponent\'s right leg while heavy on the wizar, hop left leg in line with opponent\'s toes, right leg kicks into opponent\'s right leg at the knee, use momentum and torque to finish throw',
                    'Opponent has body lock with head outside, establish right hand airmpit grip on opponent\'s left arm and left hand grip on far side elbow, circle around towards opponent\'s right leg while heavy on the head, hop left leg in line with opponent\'s toes, right leg kicks into opponent\'s right leg at the knee, use momentum and torque to finish throw',
                    'Establish right hand wizar on opponent\'s left arm, left foot replaces right, right foot kicks the inside of opponent\'s near leg, post left hand on ground and hop into opponent while raising right leg elevating hip, finish take down'],    # Standing position, standing opp, left side, takedowns
                    2:
                    ['While four-pointed with hands and feet and opponent right side body lock, angle towards opponent\'s right leg, drop low and slide through legs on left-side outer-thigh, safely grab elbow-deep grip behind opponent\'s right knee while sliding under legs, establish saddle on the right leg and finish knee bar.']  # Standing position, standing opp, left side, leg locks
                    },
                3: {1: 
                    ['Establish left hand collar tie and elbow grip, clear elbow grip up, change levels to single leg, finish take down',
                    'Establish left hand collar tie and elbow grip, push opponent\'s head over right-side leg, finish foot-sweep take down',
                    'Establish right hand collar tie and elbow grip, clear elbow grip up, change levels to single leg, finish take down',
                    'Establish right hand collar tie and elbow grip, push opponent\'s head over left-side leg, finish foot-sweep take down',
                    'Opponent has body lock with head inside, establish left hand wizar on opponent\'s right arm and right hand grip on far side elbow, circle around towards opponent\'s left leg while heavy on the wizar, hop right leg in line with opponent\'s toes, left leg kicks into opponent\'s left leg at the knee, use momentum and torque to finish throw',
                    'Opponent has body lock with head inside, establish right hand wizar on opponent\'s left arm and left hand grip on far side elbow, circle around towards opponent\'s right leg while heavy on the wizar, hop left leg in line with opponent\'s toes, right leg kicks into opponent\'s right leg at the knee, use momentum and torque to finish throw',
                    'Opponent has body lock with head outside, establish right hand airmpit grip on opponent\'s left arm and left hand grip on far side elbow, circle around towards opponent\'s right leg while heavy on the head, hop left leg in line with opponent\'s toes, right leg kicks into opponent\'s right leg at the knee, use momentum and torque to finish throw'
                    'Opponent has body lock with head outside, establish left hand airmpit grip on opponent\'s right arm and right hand grip on far side elbow, circle around towards opponent\'s left leg while heavy on the head, hop right leg in line with opponent\'s toes, left leg kicks into opponent\'s left leg at the knee, use momentum and torque to finish throw',
                    'Establish right hand wizar on opponent\'s left arm, left foot replaces right, right foot kicks the inside of opponent\'s near leg, post left hand on ground and hop into opponent while raising right leg elevating hip, finish take down',
                    'Establish left hand wizar on opponent\'s right arm, right foot replaces left, left foot kicks the inside of opponent\'s near leg, post right hand on ground and hop into opponent while raising left leg elevating hip, finish take down'],    # Standing position, standing opp, both sides, takedowns
                    2: 
                    ['While four-pointed with hands and feet and opponent right side body lock, angle towards opponent\'s right leg, drop low and slide through legs on left-side outer-thigh, safely grab elbow-deep grip behind opponent\'s right knee while sliding under legs, establish saddle on the right leg and finish knee bar.',
                    'While four-pointed with hands and feet and opponent left side body lock, angle towards opponent\'s left leg, drop low and slide through legs on right-side outer-thigh, safely grab elbow-deep grip behind opponent\'s left knee while sliding under legs, establish saddle on the left leg and finish knee bar.']    # Standing position, standing opp, both sides, leg locks
                    }
                }
            },
        5: {1: {1: 
                ['Two hooks in, fall to right side, finish right arm rear-naked-choke',
                'Two hooks in, fall to right side establishing body triangle, finish right arm rear-naked-choke',
                'Two hooks in, fall to right side establishing body triangle, right side kimura grip, transition to arm bar position, leg wrestle sweep back into back control, finish right arm rear-naked-choke'],   # Back control, right side, RNC
                2: 
                ['Two hooks in, fall to right side establishing body triangle, right side kimura grip, transition to arm bar position and finish']  # Back control, right side, armbar
                },
            2: {1: 
                ['Two hooks in, fall to left side, finish left arm rear-naked-choke',
                'Two hooks in, fall to left side establishing body triangle, finish left arm rear-naked-choke',
                'Two hooks in, fall to left side establishing body triangle, left side kimura grip, transition to arm bar position, leg wrestle sweep back into back control, finish left arm rear-naked-choke'],  # Back contol, left side, RNC
                2:
                ['Two hooks in, fall to left side establishing body triangle, left side kimura grip, transition to arm bar position and finish']  # Back control, left side, armbar
                },
            3: {1:
                ['Two hooks in, fall to right side, finish right arm rear-naked-choke',
                'Two hooks in, fall to right side establishing body triangle, finish right arm rear-naked-choke',
                'Two hooks in, fall to left side, finish left arm rear-naked-choke',
                'Two hooks in, fall to left side establishing body triangle, finish left arm rear-naked-choke',
                'Two hooks in, fall to right side establishing body triangle, right side kimura grip, transition to arm bar position, leg wrestle sweep back into back control, finish right arm rear-naked-choke',
                'Two hooks in, fall to left side establishing body triangle, left side kimura grip, transition to arm bar position, leg wrestle sweep back into back control, finish left arm rear-naked-choke'],    # Back control, both sides, RNC
                2:
                ['Two hooks in, fall to right side establishing body triangle, right side kimura grip, transition to arm bar position and finish',
                'Two hooks in, fall to left side establishing body triangle, left side kimura grip, transition to arm bar position and finish']   # Back control, both sides, armbar
                }
            },
        6: {1: {1: {1:
                    ['Left leg in between, right leg stapled over top, secure left-hand grip around opponent\'s head, twist opponent, slide off and finish arm triangle',
                    'Left leg in between, right leg stapled over top, secure left-hand grip around opponent\'s head, slide arm around opponent\'s neck, stay on top with pressure and finish arm-in ezekiel',
                    'Left leg in between, right leg stapled over top, opponent bases up on far elbow, secure Dagestani grip and break posture down, use right shoulder and under left arm to roll over opponent, lock up legs and hip into opponent left hip, finish rear naked choke']   # Leg ride, leg in-between, right side, strangles
                    },
                2: {1:
                    ['Right leg in between, left leg stapled over top, secure right-hand grip around opponent\'s head, twist opponent, slide off and finish arm triangle',
                    'Right leg in between, left leg stapled over top, secure right-hand grip around opponent\'s head, slide arm around opponent\'s neck, stay on top with pressure and finish arm-in ezekiel',
                    'Right leg in between, left leg stapled over top, opponent bases up on far elbow, secure Dagestani grip and break posture down, use left shoulder and under right arm to roll over opponent, lock up legs and hip into opponent right hip, finish rear naked choke']  # Leg ride, leg in-between, left side, strangles
                    },
                3: {1:
                    ['Left leg in between, right leg stapled over top, secure left-hand grip around opponent\'s head, twist opponent, slide off and finish arm triangle',
                    'Left leg in between, right leg stapled over top, secure left-hand grip around opponent\'s head, slide arm around opponent\'s neck, stay on top with pressure and finish arm-in ezekiel',
                    'Right leg in between, left leg stapled over top, secure right-hand grip around opponent\'s head, twist opponent, slide off and finish arm triangle',
                    'Right leg in between, left leg stapled over top, secure right-hand grip around opponent\'s head, slide arm around opponent\'s neck, stay on top with pressure and finish arm-in ezekiel',
                    'Left leg in between, right leg stapled over top, opponent bases up on far elbow, secure Dagestani grip and break posture down, use right shoulder and under left arm to roll over opponent, lock up legs and hip into opponent left hip, finish rear naked choke',
                    'Right leg in between, left leg stapled over top, opponent bases up on far elbow, secure Dagestani grip and break posture down, use left shoulder and under right arm to roll over opponent, lock up legs and hip into opponent right hip, finish rear naked choke']  # Leg ride, leg in-between, both sides, strangles
                    }            
                },
            2: {1: {1:
                    ['Left leg stapled over top, secure left-hand grip around opponent\'s head, twist opponent, slide off and finish arm triangle',
                    'Left leg stapled over top, secure left-hand grip around opponent\'s head, slide arm around opponent\'s neck, stay on top with pressure and finish arm-in ezekiel'],    # Leg ride, leg over top, right side, strangles
                    2:
                    ['Left leg stapled over top, secure left-hand placement under oppenent\'s left arm and behind head, secure kimura grip, swing right leg around over face, fully transition and fall over to finish arm bar']    # Leg ride, leg over top, right side, arm locks
                    },
               2: {1:
                    ['Right leg stapled over top, secure right-hand grip around opponent\'s head, twist opponent, slide off and finish arm triangle',
                    'Right leg stapled over top, secure right-hand grip around opponent\'s head, slide arm around opponent\'s neck, stay on top with pressure and finish arm-in ezekiel'],   # Leg ride, leg over the top, left side, strangles
                    2:
                    ['Right leg stapled over top, secure right-hand placement under oppenent\'s right arm and behind head, secure kimura grip, swing left leg around over face, fully transition and fall over to finish arm bar']    # Leg ride, leg over top, left side, arm locks
                    },
                3: {1:
                    ['Left leg stapled over top, secure left-hand grip around opponent\'s head, twist opponent, slide off and finish arm triangle',
                    'Left leg stapled over top, secure left-hand grip around opponent\'s head, slide arm around opponent\'s neck, stay on top with pressure and finish arm-in ezekiel',
                    'Right leg stapled over top, secure right-hand grip around opponent\'s head, twist opponent, slide off and finish arm triangle',
                    'Right leg stapled over top, secure right-hand grip around opponent\'s head, slide arm around opponent\'s neck, stay on top with pressure and finish arm-in ezekiel'],   # Leg ride, leg over top, both sides, strangles
                    2:
                    ['Left leg stapled over top, secure left-hand placement under oppenent\'s left arm and behind head, secure kimura grip, swing right leg around over face, fully transition and fall over to finish arm bar',
                    'Right leg stapled over top, secure right-hand placement under oppenent\'s right arm and behind head, secure kimura grip, swing left leg around over face, fully transition and fall over to finish arm bar']   # Leg ride, leg over top, both sides, arm locks
                    }
                }
            },
        7: {1: {1: {1:
                    ['Right arm over opponent\'s right leg for the over wrap, roll to right side keeping knees close to chest, secure opponent\'s top leg between legs and cross feet, secure leg under armpit, optionally secure opponent\'s bottom leg under left leg, finish knee bar']  # Turtle guard, opponent rear bodylock, right side, leg locks
                    },
                2: {1: 
                    ['Left arm over opponent\'s left leg for the over wrap, roll to left side keeping knees close to chest, secure opponent\'s top leg between legs and cross feet, secure leg under armpit, optionally secure opponent\'s bottom leg under right leg, finish knee bar']    # Turtle guard, opponent rear bodylock, left side, leg locks
                    },    
                3: {1:
                    ['Right arm over opponent\'s right leg for the over wrap, roll to right side keeping knees close to chest, secure opponent\'s top leg between legs and cross feet, secure leg under armpit, optionally secure opponent\'s bottom leg under left leg, finish knee bar',
                    'Left arm over opponent\'s left leg for the over wrap, roll to left side keeping knees close to chest, secure opponent\'s top leg between legs and cross feet, secure leg under armpit, optionally secure opponent\'s bottom leg under right leg, finish knee bar']     # Turtle guard, opponent rear bodylock, both sides, leg locks
                    }
                },
            2: {1: {1:
                    ['With left leg between opponent\'s legs, straighten right leg and roll onto left shoulder grabbing a deep scoop grip with left arm behind opponent\'s right knee, continue roll momentum using right leg to extend and push opponent away, establish grip on opponent\'s right heel with right hand and pull foot up towards right shoulder while hipping up and crossing legs, finish knee bar']  # Turtle guard, leg between opponent rear body lock, right side, leg locks
                    },
                2: {1:
                    ['With right leg between opponent\'s legs, straighten left leg and roll onto right shoulder grabbing a deep scoop grip with right arm behind opponent\'s left knee, continue roll momentum using left leg to extend and push opponent away, establish grip on opponent\'s left heel with left hand and pull foot up towards left shoulder while hipping up and crossing legs, finish knee bar']  # Turtle guard, leg between opponent rear body lock, left side, leg locks
                    },
                3: {1:
                    ['With left leg between opponent\'s legs, straighten right leg and roll onto left shoulder grabbing a deep scoop grip with left arm behind opponent\'s right knee, continue roll momentum using right leg to extend and push opponent away, establish grip on opponent\'s right heel with right hand and pull foot up towards right shoulder while hipping up and crossing legs, finish knee bar',
                    'With right leg between opponent\'s legs, straighten left leg and roll onto right shoulder grabbing a deep scoop grip with right arm behind opponent\'s left knee, continue roll momentum using left leg to extend and push opponent away, establish grip on opponent\'s left heel with left hand and pull foot up towards left shoulder while hipping up and crossing legs, finish knee bar']  # Turtle guard, leg between opponent rear body lock, both sides, leg locks
                    }
                }
            },
        8: {1: {1:
                ['With left hand, sit up while grabbing opponent\'s left knee, spin around and tuck left foot under opponent\'s butt while sitting on chest, while spinning in one motion, sit off to side of opponent securing a left lat knee bar, cross feet and finish',
                'With left hand, sit up while grabbing opponent\'s left knee, spin around and tuck left foot under opponent\'s butt while sitting on chest, option 2, use right arm to catch opponent\'s right foot with elbow grip, fall to right side while tucking opponent\'s right foot under left leg behind knee, cross feet and finish left lat knee bar',
                'Slide left knee back to inside position turning on to left side, simultaneously right hand grab opponent\'s left heel and lift towards right shoulder while twisting their foot to the right, place left foot on lower abdoben pushing away opponent while pulling right leg towards chest, pinching legs together, finish sheer knee bar']  # 50/50, right side, leg locks
                },   
            2: {1:
                ['With right hand, sit up while grabbing opponent\'s right knee, spin around and tuck right foot under opponent\'s butt while sitting on chest, while spinning in one motion, sit off to side of opponent securing a right lat knee bar, cross feet and finish',
                'With right hand, sit up while grabbing opponent\'s right knee, spin around and tuck right foot under opponent\'s butt while sitting on chest, option 2, use left arm to catch opponent\'s left foot with elbow grip, fall to left side while tucking opponent\'s left foot under right leg behind knee, cross feet and finish right lat knee bar',
                'Slide right knee back to inside position turning on to right side, simultaneously left hand grab opponent\'s right heel and lift towards left shoulder while twisting their foot to the left, place right foot on lower abdoben pushing away opponent while pulling left leg towards chest, pinching legs together, finish sheer knee bar']  # 50/50, left side, leg locks
                },   
            3: {1:
                ['With right hand, sit up while grabbing opponent\'s right knee, spin around and tuck right foot under opponent\'s butt while sitting on chest, while spinning in one motion, sit off to side of opponent securing a right lat knee bar, cross feet and finish',
                'With left hand, sit up while grabbing opponent\'s left knee, spin around and tuck left foot under opponent\'s butt while sitting on chest, while spinning in one motion, sit off to side of opponent securing a left lat knee bar, cross feet and finish',
                'With right hand, sit up while grabbing opponent\'s right knee, spin around and tuck right foot under opponent\'s butt while sitting on chest, option 2, use left arm to catch opponent\'s left foot with elbow grip, fall to left side while tucking opponent\'s left foot under right leg behind knee, cross feet and finish right lat knee bar',
                'With left hand, sit up while grabbing opponent\'s left knee, spin around and tuck left foot under opponent\'s butt while sitting on chest, option 2, use right arm to catch opponent\'s right foot with elbow grip, fall to right side while tucking opponent\'s right foot under left leg behind knee, cross feet and finish left lat knee bar',
                'Slide right knee back to inside position turning on to right side, simultaneously left hand grab opponent\'s right heel and lift towards left shoulder while twisting their foot to the left, place right foot on lower abdoben pushing away opponent while pulling left leg towards chest, pinching legs together, finish sheer knee bar',
                'Slide left knee back to inside position turning on to left side, simultaneously right hand grab opponent\'s left heel and lift towards right shoulder while twisting their foot to the right, place left foot on lower abdoben pushing away opponent while pulling right leg towards chest, pinching legs together, finish sheer knee bar']  # 50/50, both sides, leg locks
                }    
            },
        9: {1: {1: 
                ['Hook left arm eblow-deep behind opponent\'s right leg, with right leg, hook foot on inside of opponent\'s left ankle, cross left leg over right and flare opponent\'s leg out to the side for correct angle on knee, bridge up while gripping hands around opponent\'s waist to finish dog bar']  # Deep half guard, right side, leg locks
                },
            2: {1:
                ['Hook right arm eblow-deep behind opponent\'s left leg, with left leg, hook foot on inside of opponent\'s right ankle, cross right leg over left and flare opponent\'s leg out to the side for correct angle on knee, bridge up while gripping hands around opponent\'s waist to finish dog bar']  # Deep half guard, left side, leg locks
                },
            3: {1: 
                ['Hook left arm eblow-deep behind opponent\'s right leg, with right leg, hook foot on inside of opponent\'s left ankle, cross left leg over right and flare opponent\'s leg out to the side for correct angle on knee, bridge up while gripping hands around opponent\'s waist to finish dog bar',
                'Hook right arm eblow-deep behind opponent\'s left leg, with left leg, hook foot on inside of opponent\'s right ankle, cross right leg over left and flare opponent\'s leg out to the side for correct angle on knee, bridge up while gripping hands around opponent\'s waist to finish dog bar']  # Deep half guard, both sides, leg locks
                }
            },
        10: {1: {1:
                ['Establish elbow-deep grip with left arm behind opponent\'s right knee, place right hand on opponent\'s right lat, swing right leg wide outward and spin under opponent with hips elevated, use momentum and left leg to bump opponent forward until their knee is in hip pocket area, cross legs, isolate and prevent foot rotation, finish knee bar',
                'Establish elbow-deep grip with left arm behind opponent\'s right knee, remove knee shield and kick right leg onto left side and come up as far as possible, bumping butt into opponent\'s chest to off-balance them back, use right hand to grab opponent\'s heel and pull foot to chest, opponent sits to their outside hip, cross feet and lift their foot up to right shoulder, finish knee bar',
                'Establish elbow-deep grip with left arm behind opponent\'s right knee, remove knee shield and kick right leg onto left side and come up as far as possible, bumping butt into opponent\'s chest to off-balance them back, use right hand to grab opponent\'s heel and pull foot to chest, opponent rolls over their right shoulder, follow leg and cross feet, finish knee bar']  # Knee shield bottom, right side, leg locks
                },
            2: {1:
                ['Establish elbow-deep grip with right arm behind opponent\'s left knee, place left hand on opponent\'s left lat, swing left leg wide outward and spin under opponent with hips elevated, use momentum and right leg to bump opponent forward until their knee is in hip pocket area, cross legs, isolate and prevent foot rotation, finish knee bar',
                'Establish elbow-deep grip with right arm behind opponent\'s left knee, remove knee shield and kick left leg onto right side and come up as far as possible, bumping butt into opponent\'s chest to off-balance them back, use left hand to grab opponent\'s heel and pull foot to chest, opponent sits to their outside hip, cross feet and lift their foot up to left shoulder, finish knee bar',
                'Establish elbow-deep grip with right arm behind opponent\'s left knee, remove knee shield and kick left leg onto right side and come up as far as possible, bumping butt into opponent\'s chest to off-balance them back, use left hand to grab opponent\'s heel and pull foot to chest, opponent rolls over their left shoulder, follow leg and cross feet, finish knee bar']  # Knee shield bottom, left side, leg locks
                },
            3: {1:
                ['Establish elbow-deep grip with left arm behind opponent\'s right knee, place right hand on opponent\'s right lat, swing right leg wide outward and spin under opponent with hips elevated, use momentum and left leg to bump opponent forward until their knee is in hip pocket area, cross legs, isolate and prevent foot rotation, finish knee bar',
                'Establish elbow-deep grip with right arm behind opponent\'s left knee, place left hand on opponent\'s left lat, swing left leg wide outward and spin under opponent with hips elevated, use momentum and right leg to bump opponent forward until their knee is in hip pocket area, cross legs, isolate and prevent foot rotation, finish knee bar',
                'Establish elbow-deep grip with left arm behind opponent\'s right knee, remove knee shield and kick right leg onto left side and come up as far as possible, bumping butt into opponent\'s chest to off-balance them back, use right hand to grab opponent\'s heel and pull foot to chest, opponent sits to their outside hip, cross feet and lift their foot up to right shoulder, finish knee bar',
                'Establish elbow-deep grip with right arm behind opponent\'s left knee, remove knee shield and kick left leg onto right side and come up as far as possible, bumping butt into opponent\'s chest to off-balance them back, use left hand to grab opponent\'s heel and pull foot to chest, opponent sits to their outside hip, cross feet and lift their foot up to left shoulder, finish knee bar',
                'Establish elbow-deep grip with left arm behind opponent\'s right knee, remove knee shield and kick right leg onto left side and come up as far as possible, bumping butt into opponent\'s chest to off-balance them back, use right hand to grab opponent\'s heel and pull foot to chest, opponent rolls over their right shoulder, follow leg and cross feet, finish knee bar',
                'Establish elbow-deep grip with right arm behind opponent\'s left knee, remove knee shield and kick left leg onto right side and come up as far as possible, bumping butt into opponent\'s chest to off-balance them back, use left hand to grab opponent\'s heel and pull foot to chest, opponent rolls over their left shoulder, follow leg and cross feet, finish knee bar']  # Knee shield bottom, both sides, leg locks
                }
            },
        11: {1: {1:
                ['Establish under-leg scoop grip with left arm on opponent\'s top leg, knee slide right knee across to other side and right-hand post, complete rotation by falling to right hip and use left leg to lift opponent\'s hips so right leg can clear to other side, finish knee bar',
                'Establish under-leg scoop grip with left arm on opponent\'s top leg, knee slide right knee across to other side and right-hand post, opponent turns away, switch left arm grip to right arm, follow opponent turn by falling to left hip while simultaneusly grabbing opponent\'s bottom ankle with left hand, securing it under right leg for double leg control, finish right lat knee bar']  # Half guard top, right side, leg locks
                },
            2: {1:
                ['Establish under-leg scoop grip with right arm on opponent\'s top leg, knee slide left knee across to other side and left-hand post, complete rotation by falling to left hip and use right leg to lift opponent\'s hips so left leg can clear to other side, finish knee bar',
                'Establish under-leg scoop grip with right arm on opponent\'s top leg, knee slide left knee across to other side and left-hand post, opponent turns away, switch right arm grip to left arm, follow opponent turn by falling to right hip while simultaneusly grabbing opponent\'s bottom ankle with right hand, securing it under left leg for double leg control, finish left lat knee bar']  # Half guard top, left side, leg locks
                },
            3: {1: 
                ['Establish under-leg scoop grip with left arm on opponent\'s top leg, knee slide right knee across to other side and right-hand post, complete rotation by falling to right hip and use left leg to lift opponent\'s hips so right leg can clear to other side, finish knee bar',
                'Establish under-leg scoop grip with right arm on opponent\'s top leg, knee slide left knee across to other side and left-hand post, complete rotation by falling to left hip and use right leg to lift opponent\'s hips so left leg can clear to other side, finish knee bar',
                'Establish under-leg scoop grip with left arm on opponent\'s top leg, knee slide right knee across to other side and right-hand post, opponent turns away, switch left arm grip to right arm, follow opponent turn by falling to left hip while simultaneusly grabbing opponent\'s bottom ankle with left hand, securing it under right leg for double leg control, finish right lat knee bar',
                'Establish under-leg scoop grip with right arm on opponent\'s top leg, knee slide left knee across to other side and left-hand post, opponent turns away, switch right arm grip to left arm, follow opponent turn by falling to right hip while simultaneusly grabbing opponent\'s bottom ankle with right hand, securing it under left leg for double leg control, finish left lat knee bar']  # Half guard top, both sides, leg locks
                }
            },
        12: {1: {1:
                ['As opponent comes in to establish knee-on-belly, use right-hand frame under left side armpit and left-hand frame behind opponent\'s right knee, guide opponent past diagonally to right side while pulling head out to behind opponent, pass the left-hand grip to right-hand, push far leg with right hand and pull near leg with left hand to turn and lift hips up to throw left leg over behind opponent\'s left leg reap-style, pinch legs together and hip up into their knee, finish left lat knee bar']  # Knee on belly bottom, right side, leg locks
                },
            2: {1: 
                ['As opponent comes in to establish knee-on-belly, use left-hand frame under right side armpit and right-hand frame behind opponent\'s left knee, guide opponent past diagonally to left side while pulling head out to behind opponent, pass the right-hand grip to left-hand, push far leg with left hand and pull near leg with right hand to turn and lift hips up to throw right leg over behind opponent\'s right leg reap-style, pinch legs together and hip up into their knee, finish right lat knee bar']  # Knee on belly bottom, left side, leg locks
                },
            3: {1: 
                ['As opponent comes in to establish knee-on-belly, use left-hand frame under right side armpit and right-hand frame behind opponent\'s left knee, guide opponent past diagonally to left side while pulling head out to behind opponent, pass the right-hand grip to left-hand, push far leg with left hand and pull near leg with right hand to turn and lift hips up to throw right leg over behind opponent\'s right leg reap-style, pinch legs together and hip up into their knee, finish right lat knee bar',
                'As opponent comes in to establish knee-on-belly, use right-hand frame under left side armpit and left-hand frame behind opponent\'s right knee, guide opponent past diagonally to right side while pulling head out to behind opponent, pass the left-hand grip to right-hand, push far leg with right hand and pull near leg with left hand to turn and lift hips up to throw left leg over behind opponent\'s left leg reap-style, pinch legs together and hip up into their knee, finish left lat knee bar']  # Knee on belly bottom, both sides leg locks
                }
            },
        13: {1: {1: 
                ['Opponent pendulums left leg pushing to get away, go with this momentum and windshield-wipe feet so right foot is stapled across opponent\'s bottom leg, reach around with left arm to grab opponent\'s left leg, step over with left leg, fall to right side and finish left lat knee bar',
                'Opponent pendulums left leg pushing to get away, go with this momentum and windshield-wipe feet so right foot is stapled across opponent\'s bottom leg, reach around with left arm to grab opponent\'s left leg, step over with left leg and swing it all the way under opponent\'s butt, using momentum fall to left side and finish left lat knee bar']  # Leg drag, right side, leg locks
                },
            2: {1: 
                ['Opponent pendulums right leg pushing to get away, go with this momentum and windshield-wipe feet so left foot is stapled across opponent\'s bottom leg, reach around with right arm to grab opponent\'s right leg, step over with right leg, fall to left side and finish right lat knee bar',
                'Opponent pendulums right leg pushing to get away, go with this momentum and windshield-wipe feet so left foot is stapled across opponent\'s bottom leg, reach around with right arm to grab opponent\'s right leg, step over with right leg and swing it all the way under opponent\'s butt, using momentum fall to right side and finish right lat knee bar']  # Leg drag, left side, leg locks
                },
            3: {1: 
                ['Opponent pendulums right leg pushing to get away, go with this momentum and windshield-wipe feet so left foot is stapled across opponent\'s bottom leg, reach around with right arm to grab opponent\'s right leg, step over with right leg, fall to left side and finish right lat knee bar',
                'Opponent pendulums right leg pushing to get away, go with this momentum and windshield-wipe feet so left foot is stapled across opponent\'s bottom leg, reach around with right arm to grab opponent\'s right leg, step over with right leg and swing it all the way under opponent\'s butt, using momentum fall to right side and finish right lat knee bar',
                'Opponent pendulums left leg pushing to get away, go with this momentum and windshield-wipe feet so right foot is stapled across opponent\'s bottom leg, reach around with left arm to grab opponent\'s left leg, step over with left leg, fall to right side and finish left lat knee bar',
                'Opponent pendulums left leg pushing to get away, go with this momentum and windshield-wipe feet so right foot is stapled across opponent\'s bottom leg, reach around with left arm to grab opponent\'s left leg, step over with left leg and swing it all the way under opponent\'s butt, using momentum fall to left side and finish left lat knee bar']  # Leg drag, both sides, leg locks
                }
            },
        14: {1: {1: {1: 
                    ['With left knee on belly, use left hand to secure a underhand grip behind opponent\'s right tricep close to armpit, simultaneously lift opponent onto their side and spin around their head towards the back, place top of right foot behind opponent\'s right shoulder blade, secure top arm and finish arm bar',
                    'With left knee on belly, grab opponent\'s left wrist with right hand, place left hand on their far hip, distribute weight to the left and swing left foot under near-side shoulder blade, simultaneously swing right leg over opponent\'s face, finish arm bar']  # Knee on belly top, standard position, right side, arm locks
                    },
                2: {1:
                    ['With right knee on belly, use right hand to secure a underhand grip behind opponent\'s left tricep close to armpit, simultaneously lift opponent onto their side and spin around their head towards the back, place top of left foot behind opponent\'s left shoulder blade, secure top arm and finish arm bar',
                    'With right knee on belly, grab opponent\'s right wrist with left hand, place right hand on their far hip, distribute weight to the right and swing right foot under near-side shoulder blade, simultaneously swing left leg over opponent\'s face, finish arm bar']  # Knee on belly top, standard position, left side, arm locks
                    },
                3: {1: 
                    ['With left knee on belly, use left hand to secure a underhand grip behind opponent\'s right tricep close to armpit, simultaneously lift opponent onto their side and spin around their head towards the back, place top of right foot behind opponent\'s right shoulder blade, secure top arm and finish arm bar',
                    'With right knee on belly, use right hand to secure a underhand grip behind opponent\'s left tricep close to armpit, simultaneously lift opponent onto their side and spin around their head towards the back, place top of left foot behind opponent\'s left shoulder blade, secure top arm and finish arm bar',
                    'With left knee on belly, grab opponent\'s left wrist with right hand, place left hand on their far hip, distribute weight to the left and swing left foot under near-side shoulder blade, simultaneously swing right leg over opponent\'s face, finish arm bar',
                    'With right knee on belly, grab opponent\'s right wrist with left hand, place right hand on their far hip, distribute weight to the right and swing right foot under near-side shoulder blade, simultaneously swing left leg over opponent\'s face, finish arm bar']  # Knee on belly top, standard position, both sides, arm locks
                    }
                },
            2: {1: {1: 
                    ['With right knee on belly, roll to right side while peeking through the legs with both arms and establishing a left lat grip on opponent\'s left leg, keep right foot shallow into opponent\'s groin, throw left leg reap over opponent\'s top leg, finish left lat knee bar']  # Knee on belly top, reverse position, right side, leg locks
                    },
                2: {1:
                    ['With left knee on belly, roll to left side while peeking through the legs with both arms and establishing a right lat grip on opponent\'s right leg, keep left foot shallow into opponent\'s groin, throw right leg reap over opponent\'s top leg, finish right lat knee bar']  # Knee on belly top, reverse position, left side, leg locks
                    },
                3: {1: 
                    ['With left knee on belly, roll to left side while peeking through the legs with both arms and establishing a right lat grip on opponent\'s right leg, keep left foot shallow into opponent\'s groin, throw right leg reap over opponent\'s top leg, finish right lat knee bar',
                    'With right knee on belly, roll to right side while peeking through the legs with both arms and establishing a left lat grip on opponent\'s left leg, keep right foot shallow into opponent\'s groin, throw left leg reap over opponent\'s top leg, finish left lat knee bar']  # Knee on belly top, reverse position, both sides, leg locks
                    }
                }
            },
        15: {1: {1: {1: 
                    ['Secure left hand grip on opponent\'s lapel, hip up and push opponent over their left side to sweep, tuck right elbow to hip, establish proper sandwich control and finish straight foot lock',
                    'Secure left hand grip on opponent\'s lapel, opponent breaks lapel grip, immediately grab far leg heel and double leg sweep, tuck right elbow to hip, establish proper sandwich control and finish straight foot lock',
                    'Opponent posts both hands and turns off to the left side, remove butterfly leg, swing free leg and simultaneously use other leg posted on hip to rotate under opponent, secure elbow grip behind opponent\'s right heel and begin lifting opponent\'s legs, shifting their weight to their hands, rotate legs and roll to right side for sweep, reestablish butterfly ashi, finish straight foot lock',
                    'Secure left hand grip on opponent\'s lapel, opponent breaks grip and grabs sleeve, use left foot to pull behind elbow and pummel under to grip opponent\'s wrist, remove butterfly leg and establish a half day la heeva pressuring into opponent\'s lower left knee, place left leg behind opponent\'s right knee, get square with opponent and sweep them back, slightly scoot back and establish de la heeva with right leg, keeping other grips finish straight foot lock',
                    'Secure left hand grip on opponent\'s lapel, opponent breaks grip and grabs sleeve, use left foot to pull behind elbow and pummel under to grip opponent\'s wrist, remove butterfly leg and establish a half day la heeva pressuring into opponent\'s lower left knee, place left leg behind opponent\'s right knee, get square with opponent and sweep them back, cannot establish day la heeva, re pummel to butterfly ashi and finish straight foot lock',
                    'Opponent begins pressuring into legs, applying more weight on attacked leg, switch to shallow kay guard, push opponent\'s far leg away with right leg making scooped leg light, simultaneously turn off that push towards opponent\'s front side while lifting right elbow and shoulder torquing opponent\'s leg onto chest, with opponent off-balanced onto hands, bring legs over the back and finish knee bar']  # Butterfly ashi, standing opp, right side, leg locks
                    },
                2: {1: 
                    ['Secure right hand grip on opponent\'s lapel, hip up and push opponent over their right side to sweep, tuck left elbow to hip, establish proper sandwich control and finish straight foot lock',
                    'Secure right hand grip on opponent\'s lapel, opponent breaks lapel grip, immediately grab far leg heel and double leg sweep, tuck left elbow to hip, establish proper sandwich control and finish straight foot lock',
                    'Opponent posts both hands and turns off to the right side, remove butterfly leg, swing free leg and simultaneously use other leg posted on hip to rotate under opponent, secure elbow grip behind opponent\'s left heel and begin lifting opponent\'s legs, shifting their weight to their hands, rotate legs and roll to left side for sweep, reestablish butterfly ashi, finish straight foot lock',
                    'Secure right hand grip on opponent\'s lapel, opponent breaks grip and grabs sleeve, use right foot to pull behind elbow and pummel under to grip opponent\'s wrist, remove butterfly leg and establish a half day la heeva pressuring into opponent\'s lower right knee, place right leg behind opponent\'s left knee, get square with opponent and sweep them back, slightly scoot back and establish de la heeva with left leg, keeping other grips finish straight foot lock',
                    'Secure right hand grip on opponent\'s lapel, opponent breaks grip and grabs sleeve, use right foot to pull behind elbow and pummel under to grip opponent\'s wrist, remove butterfly leg and establish a half day la heeva pressuring into opponent\'s lower right knee, place right leg behind opponent\'s left knee, get square with opponent and sweep them back, cannot establish de la heeva, re pummel to butterfly ashi and finish straight foot lock',
                    'Opponent begins pressuring into legs, applying more weight on attacked leg, switch to shallow kay guard, push opponent\'s far leg away with left leg making scooped leg light, simultaneously turn off that push towards opponent\'s front side while lifting left elbow and shoulder torquing opponent\'s leg onto chest, with opponent off-balanced onto hands, bring legs over the back and finish knee bar']  # Butterfly ashi, standing opp, left side, leg locks
                    },
                3: {1: 
                    ['Secure left hand grip on opponent\'s lapel, hip up and push opponent over their left side to sweep, tuck right elbow to hip, establish proper sandwich control and finish straight foot lock',
                    'Secure left hand grip on opponent\'s lapel, opponent breaks lapel grip, immediately grab far leg heel and double leg sweep, tuck right elbow to hip, establish proper sandwich control and finish straight foot lock',
                    'Opponent posts both hands and turns off to the left side, remove butterfly leg, swing free leg and simultaneously use other leg posted on hip to rotate under opponent, secure elbow grip behind opponent\'s right heel and begin lifting opponent\'s legs, shifting their weight to their hands, rotate legs and roll to right side for sweep, reestablish butterfly ashi, finish straight foot lock',
                    'Secure left hand grip on opponent\'s lapel, opponent breaks grip and grabs sleeve, use left foot to pull behind elbow and pummel under to grip opponent\'s wrist, remove butterfly leg and establish a half day la heeva pressuring into opponent\'s lower left knee, place left leg behind opponent\'s right knee, get square with opponent and sweep them back, slightly scoot back and establish de la heeva with right leg, keeping other grips finish straight foot lock',
                    'Secure left hand grip on opponent\'s lapel, opponent breaks grip and grabs sleeve, use left foot to pull behind elbow and pummel under to grip opponent\'s wrist, remove butterfly leg and establish a half day la heeva pressuring into opponent\'s lower left knee, place left leg behind opponent\'s right knee, get square with opponent and sweep them back, cannot establish day la heeva, re pummel to butterfly ashi and finish straight foot lock',
                    'Secure right hand grip on opponent\'s lapel, hip up and push opponent over their right side to sweep, tuck left elbow to hip, establish proper sandwich control and finish straight foot lock',
                    'Secure right hand grip on opponent\'s lapel, opponent breaks lapel grip, immediately grab far leg heel and double leg sweep, tuck left elbow to hip, establish proper sandwich control and finish straight foot lock',
                    'Opponent posts both hands and turns off to the right side, remove butterfly leg, swing free leg and simultaneously use other leg posted on hip to rotate under opponent, secure elbow grip behind opponent\'s left heel and begin lifting opponent\'s legs, shifting their weight to their hands, rotate legs and roll to left side for sweep, reestablish butterfly ashi, finish straight foot lock',
                    'Secure right hand grip on opponent\'s lapel, opponent breaks grip and grabs sleeve, use right foot to pull behind elbow and pummel under to grip opponent\'s wrist, remove butterfly leg and establish a half day la heeva pressuring into opponent\'s lower right knee, place right leg behind opponent\'s left knee, get square with opponent and sweep them back, slightly scoot back and establish de la heeva with left leg, keeping other grips finish straight foot lock',
                    'Secure right hand grip on opponent\'s lapel, opponent breaks grip and grabs sleeve, use right foot to pull behind elbow and pummel under to grip opponent\'s wrist, remove butterfly leg and establish a half day la heeva pressuring into opponent\'s lower right knee, place right leg behind opponent\'s left knee, get square with opponent and sweep them back, cannot establish day la heeva, re pummel to butterfly ashi and finish straight foot lock',
                    'Opponent begins pressuring into legs, applying more weight on attacked leg, switch to shallow kay guard, push opponent\'s far leg away with right leg making scooped leg light, simultaneously turn off that push towards opponent\'s front side while lifting right elbow and shoulder torquing opponent\'s leg onto chest, with opponent off-balanced onto hands, bring legs over the back and finish knee bar',
                    'Opponent begins pressuring into legs, applying more weight on attacked leg, switch to shallow kay guard, push opponent\'s far leg away with left leg making scooped leg light, simultaneously turn off that push towards opponent\'s front side while lifting left elbow and shoulder torquing opponent\'s leg onto chest, with opponent off-balanced onto hands, bring legs over the back and finish knee bar']  # Butterfly ashi, standing opp, both sides, leg locks
                    }
                },
            2: {1: {1:
                    ['Base left hand to scoot back making opponent\'s leg closer to 90 degree angle, tuck right elbow to right hip, while pinching legs and pressing against opponent\'s hip to extend them away, establish proper sandwich control and finish straight foot lock',
                    'While square with opponent, open chest up to the sky, tuck elbow tight to body, left hand presses against opponent\'s top of shin, establish all sandwich controls, finish straight foot lock',
                    'While on left hip, expand chest open, simultaneously hip into fulcrum and establish all sandwich controls, finish straight foot lock',
                    'In a belly down position, base on head, left hand presses on top of opponent\'s shin, open up chest and keep right elbow tight against side, slowly spread legs hipping into fulcrum and opponent\'s left leg, finish straight foot lock',
                    'Establish a double elbow grip and roll opponent\'s left heel partially onto chest, establish normal sandwich controls and finish Aoki lock',
                    'Bring left leg across to other side hip and curl leg tight, post left hand and begin to come up onto opponent, remove butterfly hook and base with that leg while applying weight through left knee onto opponent, keep left foot away from opponent armpit, right hand scoop grip and rotate off to knee bar finish']  # Butterfly ashi, seated opp, right side, leg locks
                    },
                2: {1:
                    ['Base right hand to scoot back making opponent\'s leg closer to 90 degree angle, tuck left elbow to left hip, while pinching legs and pressing against opponent\'s hip to extend them away, establish proper sandwich control and finish straight foot lock',
                    'While square with opponent, open chest up to the sky, tuck elbow tight to body, right hand presses against opponent\'s top of shin, establish all sandwich controls, finish straight foot lock',
                    'While on right hip, expand chest open, simultaneously hip into fulcrum and establish all sandwich controls, finish straight foot lock',
                    'In a belly down position, base on head, right hand presses on top of opponent\'s shin, open up chest and keep left elbow tight against side, slowly spread legs hipping into fulcrum and opponent\'s right leg, finish straight foot lock',
                    'Establish a double elbow grip and roll opponent\'s right heel partially onto chest, establish normal sandwich controls and finish Aoki lock',
                    'Bring right leg across to other side hip and curl leg tight, post right hand and begin to come up onto opponent, remove butterfly hook and base with that leg while applying weight through right knee onto opponent, keep right foot away from opponent armpit, left hand scoop grip and rotate off to knee bar finish']  # Butterfly ashi, seated opp, left side, leg locks
                    },
                3: {1:
                    ['Base right hand to scoot back making opponent\'s leg closer to 90 degree angle, tuck left elbow to left hip, while pinching legs and pressing against opponent\'s hip to extend them away, establish proper sandwich control and finish straight foot lock',
                    'While square with opponent, open chest up to the sky, tuck elbow tight to body, right hand presses against opponent\'s top of shin, establish all sandwich controls, finish straight foot lock',
                    'While on right hip, expand chest open, simultaneously hip into fulcrum and establish all sandwich controls, finish straight foot lock',
                    'In a belly down position, base on head, right hand presses on top of opponent\'s shin, open up chest and keep left elbow tight against side, slowly spread legs hipping into fulcrum and opponent\'s right leg, finish straight foot lock',
                    'Base left hand to scoot back making opponent\'s leg closer to 90 degree angle, tuck right elbow to right hip, while pinching legs and pressing against opponent\'s hip to extend them away, establish proper sandwich control and finish straight foot lock',
                    'While square with opponent, open chest up to the sky, tuck elbow tight to body, left hand presses against opponent\'s top of shin, establish all sandwich controls, finish straight foot lock',
                    'While on left hip, expand chest open, simultaneously hip into fulcrum and establish all sandwich controls, finish straight foot lock',
                    'In a belly down position, base on head, left hand presses on top of opponent\'s shin, open up chest and keep right elbow tight against side, slowly spread legs hipping into fulcrum and opponent\'s left leg, finish straight foot lock',
                    'Establish a double elbow grip and roll opponent\'s left heel partially onto chest, establish normal sandwich controls and finish Aoki lock',
                    'Establish a double elbow grip and roll opponent\'s right heel partially onto chest, establish normal sandwich controls and finish Aoki lock',
                    'Bring right leg across to other side hip and curl leg tight, post right hand and begin to come up onto opponent, remove butterfly hook and base with that leg while applying weight through right knee onto opponent, keep right foot away from opponent armpit, left hand scoop grip and rotate off to knee bar finish',
                    'Bring left leg across to other side hip and curl leg tight, post left hand and begin to come up onto opponent, remove butterfly hook and base with that leg while applying weight through left knee onto opponent, keep left foot away from opponent armpit, right hand scoop grip and rotate off to knee bar finish']  # Butterfly ashi, seated opp, both sides, leg locks
                    }
                }
            },
        16: {1: {1:
                ['Left leg between opponent\'s legs right knee on hip, opponent attempts hip switch, catch them on knee and elbow frames, while turning onto right hip use right hand and elbow to push opponent away, bring right leg under opponent while throwing left leg over the top, cross legs and finish knee bar'],  # Z-guard, right side, leg locks
                2:
                ['Left leg between opponent\'s legs, opponent overextends their right arm, scoop left arm under the arm and establish a shoulder crunch on that arm, bring right knee to opponent\'s left shoulder, push with right elbow moving right knee to other side, push right knee into opponent\'s head, extend leg over opponent\'s head and immediately slide leg heavy over their back, bring right leg all the way over pinching heavy down on the shoulder, secure double wrist grip on opponent\'s hand and bring both knees on opposite sides of opponent\'s bicep, pinch legs back heel and finish arm bar over right hip',
                'Left leg between opponent\'s legs, opponent overextends their right arm, scoop left arm under the arm and establish a shoulder crunch on that arm, bring right knee to opponent\'s left shoulder, push with right elbow moving right knee to other side, push right knee into opponent\'s head, extend leg over opponent\'s head and immediately slide leg heavy over their back, bring right leg all the way over pinching heavy down on the shoulder, secure double wrist grip on opponent\'s hand and bring both knees on opposite sides of opponent\'s bicep, opponent rolls over, place right foot under and left foot over opponent\'s head, finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, back heel feet to butt while crossing feet, pull opponent\'s hand tight extending the arm, finish arm bar',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, back heel feet to butt while crossing feet, attempt arm bar, opponent rolls over, pull opponent\'s hand tight towards shoulders, finish arm bar',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, sit up to omoplata position while grabbing far lat with right hand, secure seat belt and finish omoplata',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, sit up to omoplata position while grabbing far lat with right hand, opponent rolls over, follow roll by rolling over right shoulder, land flat on back while opponent lands sitting upright, simultaneously establish a scoop grip around opponent\'s right shoulder, use left foot to slowly scoot out and away pressuring into the locked shoulder, finish omoplata',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, sit up to omoplata position while grabbing far lat with right hand, opponent rolls over, follow roll by rolling over right shoulder, land flat on back while opponent lands sitting upright, use left foot to hook opponent\'s left leg to prevent their movement and establish a scoop grip around opponent\'s right shoulder, remove hook and use left foot to slowly scoot out and away pressuring into the locked shoulder, finish omoplata',
                'Left leg between opponent\'s legs right knee on hip, right hand gently resting behind opponent\'s left elbow, opponent stands up, place left foot on far hip and pull the secured left arm in with palm facing up and elbow tucked to side, slide right leg down behind the elbow grip and using left leg slowly rotate hips to face the far leg, pressure into elbow and finish shotgun arm bar',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, strip opponent\'s grip and place arm in left lat grip, angle hips to the left and finish left lat arm bar',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, oppenent still keeps tight grip preventing arm lock, fall to right hip while back heeling hard with left leg to roll opponent over, secure postion and finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, opponent blocks right leg swing with left arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder shallow back heeling tight, bring feet together, finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, swing right leg out around to over the right shoulder shallow back heeling tight, bring feet together, finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, swing right leg out around to over the right shoulder shallow back heeling tight, bring feet together, opponent rolls over, secure right foot behind opponent\'s head and left foot over the top, finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, opponent blocks right leg swing with left arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder shallow back heeling tight, bring feet together, opponent rolls over, secure right foot behind opponent\'s head and left foot over the top, finish arm bar over right hip'],   # Z-guard, right side, arm locks
                3:
                ['Left leg between opponent\'s legs, opponent overextends their right arm, scoop left arm under the arm and establish a shoulder crunch on that arm, bring right knee to opponent\'s left shoulder, opponent reacts by grabbing right thigh with their left hand, place left foot on opponent\'s near side hip, while pushing into the hip extend right leg away and up to break leg grip, push off near side hip and rotate around into triangle position, finish triangle strangle',
                'Left leg between opponent\'s legs, establish strong subtle Zee guard setup by back heeling with bottom leg and extending with top leg, opponent is trying to pressure in, place right hand over opponent\'s left arm in the arm pit and left hand framing on far arm lower bicep, use frame to create space and pull left leg out and over the far shoulder falling back flat, lock up triangle position, underhook with left hand and rotate to triangle strangle finish',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, back heel right leg under the head around the neck, bring left leg out and behind the head collapsing opponent\'s head into the bottom leg, lock up right foot behind left knee and back heel while scissoring legs, squeeze and finish achilles triangle strangle',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, back heel right leg under the head around the neck, bring left leg out and behind the head collapsing opponent\'s head into the bottom leg, opponent pressures into you, roll over right shoulder while keeping pressure behind opponent\'s head, establish right hand scoop grip behind right side shoulder, rotate into and finish front triangle strangle',
                'Left leg between opponent\'s legs right knee on hip, opponent attempts weave pass with left arm without knee passing through, secure right hand grip behind weave arm in the arm pit, secure left hand grip on far wrist, scissor legs so left knee is brought to chest and right leg extends away breaking weave grip, fall back into triangle position, left hand scoop grip behind far shoulder and finish triangle strangle',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, shoot lower leg through gap between opponent\'s far elbow and knee, lock up left foot behind right knee keeping opponent\'s posture down, release kimura grip and climb for height to right arm grip body lock style, use right foot on ground to turn and come up more while retracting left knee, begin hipping weight into opponent\'s back and squeezing legs to finish yoko ono triangle strangle'],   # Z-guard, right side, strangles
                4:
                ['Left leg between opponent\'s legs right knee on hip, opponent attempts hip switch, catch them on knee and elbow frames, while keeping knees and elbows tight use opponent\'s momentum and kick legs up and back while rolling backwards, finish sweep on top']    # Z-guard, right side, sweeps
                },
            2: {1:
                ['Right leg between opponent\'s legs left knee on hip, opponent attempts hip switch, catch them on knee and elbow frames, while turning onto left hip use left hand and elbow to push opponent away, bring left leg under opponent while throwing right leg over the top, cross legs and finish knee bar'],   # Z-guard, left side, leg locks
                2:
                ['Right leg between opponent\'s legs, opponent overextends their left arm, scoop right arm under the arm and establish a shoulder crunch on that arm, bring left knee to opponent\'s right shoulder, push with left elbow moving left knee to other side, push left knee into opponent\'s head, extend leg over opponent\'s head and immediately slide leg heavy over their back, bring left leg all the way over pinching heavy down on the shoulder, secure double wrist grip on opponent\'s hand and bring both knees on opposite sides of opponent\'s bicep, pinch legs back heel and finish arm bar over left hip',
                'Right leg between opponent\'s legs, opponent overextends their left arm, scoop right arm under the arm and establish a shoulder crunch on that arm, bring left knee to opponent\'s right shoulder, push with left elbow moving left knee to other side, push left knee into opponent\'s head, extend leg over opponent\'s head and immediately slide leg heavy over their back, bring left leg all the way over pinching heavy down on the shoulder, secure double wrist grip on opponent\'s hand and bring both knees on opposite sides of opponent\'s bicep, opponent rolls over, place left foot under and right foot over opponent\'s head, finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, back heel feet to butt while crossing feet, pull opponent\'s hand tight extending the arm, finish arm bar',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, back heel feet to butt while crossing feet, attempt arm bar, opponent rolls over, pull opponent\'s hand tight towards shoulders, finish arm bar',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, sit up to omoplata position while grabbing far lat with left hand, secure seat belt and finish omoplata',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, sit up to omoplata position while grabbing far lat with left hand, opponent rolls over, follow roll by rolling over left shoulder, land flat on back while opponent lands sitting upright, simultaneously establish a scoop grip around opponent\'s left shoulder, use right foot to slowly scoot out and away pressuring into the locked shoulder, finish omoplata',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, sit up to omoplata position while grabbing far lat with left hand, opponent rolls over, follow roll by rolling over left shoulder, land flat on back while opponent lands sitting upright, use right foot to hook opponent\'s right leg to prevent their movement and establish a scoop grip around opponent\'s left shoulder, remove hook and use right foot to slowly scoot out and away pressuring into the locked shoulder, finish omoplata',
                'Right leg between opponent\'s legs left knee on hip, left hand gently resting behind opponent\'s right elbow, opponent stands up, place right foot on far hip and pull the secured right arm in with palm facing up and elbow tucked to side, slide left leg down behind the elbow grip and using right leg slowly rotate hips to face the far leg, pressure into elbow and finish shotgun arm bar',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, strip opponent\'s grip and place arm in right lat grip, angle hips to the right and finish right lat arm bar',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, oppenent still keeps tight grip preventing arm lock, fall to left hip while back heeling hard with right leg to roll opponent over, secure postion and finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, opponent blocks left leg swing with right arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder shallow back heeling tight, bring feet together, finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, swing left leg out around to over the left shoulder shallow back heeling tight, bring feet together, finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, swing left leg out around to over the left shoulder shallow back heeling tight, bring feet together, opponent rolls over, secure left foot behind opponent\'s head and right foot over the top, finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, opponent blocks left leg swing with right arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder shallow back heeling tight, bring feet together, opponent rolls over, secure left foot behind opponent\'s head and right foot over the top, finish arm bar over left hip'],   # Z-guard, left side, arm locks
                3:
                ['Right leg between opponent\'s legs, opponent overextends their left arm, scoop right arm under the arm and establish a shoulder crunch on that arm, bring left knee to opponent\'s right shoulder, opponent reacts by grabbing left thigh with their right hand, place right foot on opponent\'s near side hip, while pushing into the hip extend left leg away and up to break leg grip, push off near side hip and rotate around into triangle position, finish triangle strangle',
                'Right leg between opponent\'s legs, establish strong subtle Zee guard setup by back heeling with bottom leg and extending with top leg, opponent is trying to pressure in, place left hand over opponent\'s right arm in the arm pit and right hand framing on far arm lower bicep, use frame to create space and pull right leg out and over the far shoulder falling back flat, lock up triangle position, underhook with right hand and rotate to triangle strangle finish',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, back heel left leg under the head around the neck, bring right leg out and behind the head collapsing opponent\'s head into the bottom leg, lock up left foot behind right knee and back heel while scissoring legs, squeeze and finish achilles triangle strangle',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, back heel left leg under the head around the neck, bring right leg out and behind the head collapsing opponent\'s head into the bottom leg, opponent pressures into you, roll over left shoulder while keeping pressure behind opponent\'s head, establish left hand scoop grip behind left side shoulder, rotate into and finish front triangle strangle',
                'Right leg between opponent\'s legs left knee on hip, opponent attempts weave pass with right arm without knee passing through, secure left hand grip behind weave arm in the arm pit, secure right hand grip on far wrist, scissor legs so right knee is brought to chest and left leg extends away breaking weave grip, fall back into triangle position, right hand scoop grip behind far shoulder and finish triangle strangle',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, shoot lower leg through gap between opponent\'s far elbow and knee, lock up right foot behind left knee keeping opponent\'s posture down, release kimura grip and climb for height to left arm grip body lock style, use left foot on ground to turn and come up more while retracting right knee, begin hipping weight into opponent\'s back and squeezing legs to finish yoko ono triangle strangle'],   # Z-guard, left side, strangles
                4:
                ['Right leg between opponent\'s legs left knee on hip, opponent attempts hip switch, catch them on knee and elbow frames, while keeping knees and elbows tight use opponent\'s momentum and kick legs up and back while rolling backwards, finish sweep on top']    # Z-guard, left side, sweeps
                },
            3: {1:
                ['Left leg between opponent\'s legs right knee on hip, opponent attempts hip switch, catch them on knee and elbow frames, while turning onto right hip use right hand and elbow to push opponent away, bring right leg under opponent while throwing left leg over the top, cross legs and finish knee bar',
                'Right leg between opponent\'s legs left knee on hip, opponent attempts hip switch, catch them on knee and elbow frames, while turning onto left hip use left hand and elbow to push opponent away, bring left leg under opponent while throwing right leg over the top, cross legs and finish knee bar'],   # Z-guard, both sides, leg locks
                2:
                ['Left leg between opponent\'s legs, opponent overextends their right arm, scoop left arm under the arm and establish a shoulder crunch on that arm, bring right knee to opponent\'s left shoulder, push with right elbow moving right knee to other side, push right knee into opponent\'s head, extend leg over opponent\'s head and immediately slide leg heavy over their back, bring right leg all the way over pinching heavy down on the shoulder, secure double wrist grip on opponent\'s hand and bring both knees on opposite sides of opponent\'s bicep, pinch legs back heel and finish arm bar over right hip',
                'Left leg between opponent\'s legs, opponent overextends their right arm, scoop left arm under the arm and establish a shoulder crunch on that arm, bring right knee to opponent\'s left shoulder, push with right elbow moving right knee to other side, push right knee into opponent\'s head, extend leg over opponent\'s head and immediately slide leg heavy over their back, bring right leg all the way over pinching heavy down on the shoulder, secure double wrist grip on opponent\'s hand and bring both knees on opposite sides of opponent\'s bicep, opponent rolls over, place right foot under and left foot over opponent\'s head, finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, back heel feet to butt while crossing feet, pull opponent\'s hand tight extending the arm, finish arm bar',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, back heel feet to butt while crossing feet, attempt arm bar, opponent rolls over, pull opponent\'s hand tight towards shoulders, finish arm bar',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, sit up to omoplata position while grabbing far lat with right hand, secure seat belt and finish omoplata',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, sit up to omoplata position while grabbing far lat with right hand, opponent rolls over, follow roll by rolling over right shoulder, land flat on back while opponent lands sitting upright, simultaneously establish a scoop grip around opponent\'s right shoulder, use left foot to slowly scoot out and away pressuring into the locked shoulder, finish omoplata',
                'Left leg between opponent\'s legs right knee on hip, opponent reaches around back with left arm attempting under hook, secure right hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing right leg over opponent\'s left shoulder, sit up to omoplata position while grabbing far lat with right hand, opponent rolls over, follow roll by rolling over right shoulder, land flat on back while opponent lands sitting upright, use left foot to hook opponent\'s left leg to prevent their movement and establish a scoop grip around opponent\'s right shoulder, remove hook and use left foot to slowly scoot out and away pressuring into the locked shoulder, finish omoplata',
                'Left leg between opponent\'s legs right knee on hip, right hand gently resting behind opponent\'s left elbow, opponent stands up, place left foot on far hip and pull the secured left arm in with palm facing up and elbow tucked to side, slide right leg down behind the elbow grip and using left leg slowly rotate hips to face the far leg, pressure into elbow and finish shotgun arm bar',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, strip opponent\'s grip and place arm in left lat grip, angle hips to the left and finish left lat arm bar',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, oppenent still keeps tight grip preventing arm lock, fall to right hip while back heeling hard with left leg to roll opponent over, secure postion and finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, opponent blocks right leg swing with left arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder shallow back heeling tight, bring feet together, finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, swing right leg out around to over the right shoulder shallow back heeling tight, bring feet together, finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, swing right leg out around to over the right shoulder shallow back heeling tight, bring feet together, opponent rolls over, secure right foot behind opponent\'s head and left foot over the top, finish arm bar over right hip',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, opponent blocks right leg swing with left arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder shallow back heeling tight, bring feet together, opponent rolls over, secure right foot behind opponent\'s head and left foot over the top, finish arm bar over right hip',
                'Right leg between opponent\'s legs, opponent overextends their left arm, scoop right arm under the arm and establish a shoulder crunch on that arm, bring left knee to opponent\'s right shoulder, push with left elbow moving left knee to other side, push left knee into opponent\'s head, extend leg over opponent\'s head and immediately slide leg heavy over their back, bring left leg all the way over pinching heavy down on the shoulder, secure double wrist grip on opponent\'s hand and bring both knees on opposite sides of opponent\'s bicep, pinch legs back heel and finish arm bar over left hip',
                'Right leg between opponent\'s legs, opponent overextends their left arm, scoop right arm under the arm and establish a shoulder crunch on that arm, bring left knee to opponent\'s right shoulder, push with left elbow moving left knee to other side, push left knee into opponent\'s head, extend leg over opponent\'s head and immediately slide leg heavy over their back, bring left leg all the way over pinching heavy down on the shoulder, secure double wrist grip on opponent\'s hand and bring both knees on opposite sides of opponent\'s bicep, opponent rolls over, place left foot under and right foot over opponent\'s head, finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, back heel feet to butt while crossing feet, pull opponent\'s hand tight extending the arm, finish arm bar',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, back heel feet to butt while crossing feet, attempt arm bar, opponent rolls over, pull opponent\'s hand tight towards shoulders, finish arm bar',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, sit up to omoplata position while grabbing far lat with left hand, secure seat belt and finish omoplata',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, sit up to omoplata position while grabbing far lat with left hand, opponent rolls over, follow roll by rolling over left shoulder, land flat on back while opponent lands sitting upright, simultaneously establish a scoop grip around opponent\'s left shoulder, use right foot to slowly scoot out and away pressuring into the locked shoulder, finish omoplata',
                'Right leg between opponent\'s legs left knee on hip, opponent reaches around back with right arm attempting under hook, secure left hand grip behind that arm pit, frame against far arm and bring bottom leg through while throwing left leg over opponent\'s right shoulder, sit up to omoplata position while grabbing far lat with left hand, opponent rolls over, follow roll by rolling over left shoulder, land flat on back while opponent lands sitting upright, use right foot to hook opponent\'s right leg to prevent their movement and establish a scoop grip around opponent\'s left shoulder, remove hook and use right foot to slowly scoot out and away pressuring into the locked shoulder, finish omoplata',
                'Right leg between opponent\'s legs left knee on hip, left hand gently resting behind opponent\'s right elbow, opponent stands up, place right foot on far hip and pull the secured right arm in with palm facing up and elbow tucked to side, slide left leg down behind the elbow grip and using right leg slowly rotate hips to face the far leg, pressure into elbow and finish shotgun arm bar',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, strip opponent\'s grip and place arm in right lat grip, angle hips to the right and finish right lat arm bar',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, oppenent still keeps tight grip preventing arm lock, fall to left hip while back heeling hard with right leg to roll opponent over, secure postion and finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, opponent blocks left leg swing with right arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder shallow back heeling tight, bring feet together, finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, swing left leg out around to over the left shoulder shallow back heeling tight, bring feet together, finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, swing left leg out around to over the left shoulder shallow back heeling tight, bring feet together, opponent rolls over, secure left foot behind opponent\'s head and right foot over the top, finish arm bar over left hip',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, opponent blocks left leg swing with right arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder shallow back heeling tight, bring feet together, opponent rolls over, secure left foot behind opponent\'s head and right foot over the top, finish arm bar over left hip'],   # Z-guard, both sides, arm locks
                3:
                ['Left leg between opponent\'s legs, opponent overextends their right arm, scoop left arm under the arm and establish a shoulder crunch on that arm, bring right knee to opponent\'s left shoulder, opponent reacts by grabbing right thigh with their left hand, place left foot on opponent\'s near side hip, while pushing into the hip extend right leg away and up to break leg grip, push off near side hip and rotate around into triangle position, finish triangle strangle',
                'Left leg between opponent\'s legs, establish strong subtle Zee guard setup by back heeling with bottom leg and extending with top leg, opponent is trying to pressure in, place right hand over opponent\'s left arm in the arm pit and left hand framing on far arm lower bicep, use frame to create space and pull left leg out and over the far shoulder falling back flat, lock up triangle position, underhook with left hand and rotate to triangle strangle finish',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, back heel right leg under the head around the neck, bring left leg out and behind the head collapsing opponent\'s head into the bottom leg, lock up right foot behind left knee and back heel while scissoring legs, squeeze and finish achilles triangle strangle',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, transition right leg over the right shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, back heel right leg under the head around the neck, bring left leg out and behind the head collapsing opponent\'s head into the bottom leg, opponent pressures into you, roll over right shoulder while keeping pressure behind opponent\'s head, establish right hand scoop grip behind right side shoulder, rotate into and finish front triangle strangle',
                'Left leg between opponent\'s legs right knee on hip, opponent attempts weave pass with left arm without knee passing through, secure right hand grip behind weave arm in the arm pit, secure left hand grip on far wrist, scissor legs so left knee is brought to chest and right leg extends away breaking weave grip, fall back into triangle position, left hand scoop grip behind far shoulder and finish triangle strangle',
                'Left leg between opponent\'s legs right knee on hip, establish kimura grip on opponent\'s right arm, bring knee to opponent\'s right shoulder, push opponent\'s head away with knee and throw right leg over their back heavy, shoot lower leg through gap between opponent\'s far elbow and knee, lock up left foot behind right knee keeping opponent\'s posture down, release kimura grip and climb for height to right arm grip body lock style, use right foot on ground to turn and come up more while retracting left knee, begin hipping weight into opponent\'s back and squeezing legs to finish yoko ono triangle strangle',
                'Right leg between opponent\'s legs, opponent overextends their left arm, scoop right arm under the arm and establish a shoulder crunch on that arm, bring left knee to opponent\'s right shoulder, opponent reacts by grabbing left thigh with their right hand, place right foot on opponent\'s near side hip, while pushing into the hip extend left leg away and up to break leg grip, push off near side hip and rotate around into triangle position, finish triangle strangle',
                'Right leg between opponent\'s legs, establish strong subtle Zee guard setup by back heeling with bottom leg and extending with top leg, opponent is trying to pressure in, place left hand over opponent\'s right arm in the arm pit and right hand framing on far arm lower bicep, use frame to create space and pull right leg out and over the far shoulder falling back flat, lock up triangle position, underhook with right hand and rotate to triangle strangle finish',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, back heel left leg under the head around the neck, bring right leg out and behind the head collapsing opponent\'s head into the bottom leg, lock up left foot behind right knee and back heel while scissoring legs, squeeze and finish achilles triangle strangle',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, transition left leg over the left shoulder back heeling tight, opponent keeps tight grip preventing kimura finish, come up to forehead and knees, back heel left leg under the head around the neck, bring right leg out and behind the head collapsing opponent\'s head into the bottom leg, opponent pressures into you, roll over left shoulder while keeping pressure behind opponent\'s head, establish left hand scoop grip behind left side shoulder, rotate into and finish front triangle strangle',
                'Right leg between opponent\'s legs left knee on hip, opponent attempts weave pass with right arm without knee passing through, secure left hand grip behind weave arm in the arm pit, secure right hand grip on far wrist, scissor legs so right knee is brought to chest and left leg extends away breaking weave grip, fall back into triangle position, right hand scoop grip behind far shoulder and finish triangle strangle',
                'Right leg between opponent\'s legs left knee on hip, establish kimura grip on opponent\'s left arm, bring knee to opponent\'s left shoulder, push opponent\'s head away with knee and throw left leg over their back heavy, shoot lower leg through gap between opponent\'s far elbow and knee, lock up right foot behind left knee keeping opponent\'s posture down, release kimura grip and climb for height to left arm grip body lock style, use left foot on ground to turn and come up more while retracting right knee, begin hipping weight into opponent\'s back and squeezing legs to finish yoko ono triangle strangle'],   # Z-guard, both sides, strangles
                4:
                ['Left leg between opponent\'s legs right knee on hip, opponent attempts hip switch, catch them on knee and elbow frames, while keeping knees and elbows tight use opponent\'s momentum and kick legs up and back while rolling backwards, finish sweep on top',
                'Right leg between opponent\'s legs left knee on hip, opponent attempts hip switch, catch them on knee and elbow frames, while keeping knees and elbows tight use opponent\'s momentum and kick legs up and back while rolling backwards, finish sweep on top']    # Z-guard, both sides, sweeps
                }
            }
        },

    # DEFENSE
    2: 
        {1:None}    # Will be built out in v2.0
}

blitz_moves = {1: {1:
                    ['Seated guard standing opponent, left side, inside knee pull, finish knee bar',
                    'Seated guard standing opponent, right side, scoot under, sweep to footlock finish',
                    'Seated guard standing opponent, right side, inside knee pull, finish knee bar', 
                    'Seated guard standing opponent, left side, scoot under, sweep to footlock finish',
                    'Seated guard kneeling opponent, right side, hand to same-side shoulder, hop out to side with leg between opponent, invert and roll through finish knee bar',
                    'Seated guard kneeling opponent, right side, hand to same-side shoulder, hop out to side with leg between opponent, invert, roll back into opponents\'s legs, finish knee bar',
                    'Seated guard kneeling opponent, left side, hand to same-side shoulder, hop out to side with leg between opponent, invert and roll through finish knee bar',
                    'Seated guard kneeling opponent, left side, hand to same-side shoulder, hop out to side with leg between opponent, invert, roll back into opponents\'s legs, finish knee bar',
                    'Reverse Zee guard right side, finish early entry knee bar', 
                    'Reverse Zee guard right side, finish late entry knee bar',
                    'Reverse Zee guard left side, finish early entry knee bar', 
                    'Reverse Zee guard left side, finish late entry knee bar',
                    'Half guard bottom right side, inside knee up, hands to near side armpit, foot butterfly hook, extend and finish knee bar',
                    'Half guard bottom left side, inside knee up, hands to near side armpit, foot butterfly hook, extend and finish knee bar',
                    'Standing, supine opponent right side, backstep to knee bar finish',
                    'Standing, supine opponent right side, backstep to far leg footlock finish',
                    'Standing, supine opponent right side, sit down into straight footlock finish option 1',
                    'Standing, supine opponent right side, sit down into straight footlock finish upright option 2',
                    'Standing, supine opponent right side, sit down into straight footlock main finish option 3',
                    'Standing, supine opponent right side, sit down into straight footlock, transition to knee bar finish',
                    'Standing, supine opponent left side, backstep to knee bar finish',
                    'Standing, supine opponent left side, backstep to knee bar finish',
                    'Standing, supine opponent left side, backstep to far leg footlock finish',
                    'Standing, supine opponent left side, sit down into straight footlock finish option 1',
                    'Standing, supine opponent left side, sit down into straight footlock finish upright option 2',
                    'Standing, supine opponent left side, sit down into straight footlock main finish option 3',
                    'Standing, supine opponent left side, sit down into straight footlock, transition to knee bar finish',
                    'Standing, supine opponent right side, failed backstep attempt, hop over to other leg, finish knee bar',
                    'Standing, supine opponent left side, failed backstep attempt, hop over to other leg, finish knee bar',
                    'Turtle guard square rear body lock right side, over wrap leg, roll to same side, secure opponent\'s top leg for knee bar finish',
                    'Turtle guard square rear body lock left side, over wrap leg, roll to same side, secure opponent\'s top leg for knee bar finish',
                    'Turtle guard leg between rear body lock right side, roll over inside shoulder, finish knee bar',
                    'Turtle guard leg between rear body lock left side, roll over inside shoulder, finish knee bar',
                    'Fifty fifty guard left side, sit up full spin through option, finish knee bar',
                    'Fifty fifty guard right side, sit up full spin through option, finish knee bar',
                    'Fifty fifty guard left side, sit up to double leg control option, finish knee bar',
                    'Fifty fifty guard right side, sit up to double leg control option, finish knee bar',
                    'Fifty fifty guard left side, slide inside knee back, finish sheer knee bar',
                    'Fifty fifty guard right side, slide inside knee back, finish sheer knee bar',
                    'Deep half guard right side, flare opponent\'s leg out and square hips, bridge up finish dog bar',
                    'Deep half guard left side, flare opponent\'s leg out and square hips, bridge up finish dog bar',
                    'Knee shield bottom right side, kick right leg onto far side, opponent sits to their outside hip, finish knee bar',
                    'Knee shield bottom left side, kick left leg onto far side, opponent sits to their outside hip, finish knee bar',
                    'Knee shield bottom right side, kick right leg onto far side, opponent rolls over their right shoulder, finish knee bar',
                    'Knee shield bottom left side, kick left leg onto far side, opponent rolls over their left shoulder, finish knee bar',
                    'Half guard top right side, knee slide full rotation, finish knee bar',
                    'Half guard top left side, knee slide full rotation, finish knee bar',
                    'Half guard top right side, knee slide and post, opponent turns away, finish double leg control knee bar',
                    'Half guard top left side, knee slide and post, opponent turns away, finish double leg control knee bar',
                    'Leg drag left side, windshield-wipe feet, step over and fall to left side, finish lat knee bar',
                    'Leg drag left side, windshield-wipe feet, swing leg all the way through falling to right side, finish lat knee bar',
                    'Leg drag right side, windshield-wipe feet, step over and fall to right side, finish lat knee bar',
                    'Leg drag right side, windshield-wipe feet, swing leg all the way through falling to left side, finish lat knee bar',
                    'Knee on belly top reverse position left side, knee through to foot, roll to left side finish right lat knee bar',
                    'Knee on belly top reverse position right side, knee through to foot, roll to right side finish left lat knee bar',
                    'Butterfly ashi standing opponent right side, grip lapel, sweep to right side, finish straight foot lock',
                    'Butterfly ashi standing opponent right side, grip lapel, opponent breaks grip, double leg sweep, finish straight foot lock',
                    'Butterfly ashi standing opponent right side, opponent posts hands to left side, swing butterfly leg and rotate under opponent, lift opponent\'s legs and roll to right side for sweep, finish straight foot lock',
                    'Butterfly ashi standing opponent right side, grip lapel, opponent breaks grip and grabs sleeve, pummel for wrist grip, establish half day la heeva, left leg behind opponent\'s right knee, sweep, finish day la heeva straight foot lock',
                    'Butterfly ashi standing opponent right side, grip lapel, opponent breaks grip and grabs sleeve, pummel for wrist grip, establish half day la heeva, left leg behind opponent\'s right knee, sweep, finish butterfly ashi straight foot lock',
                    'Butterfly ashi standing opponent left side, grip lapel, sweep to left side, finish straight foot lock',
                    'Butterfly ashi standing opponent left side, grip lapel, opponent breaks grip, double leg sweep, finish straight foot lock',
                    'Butterfly ashi standing opponent left side, opponent posts hands to right side, swing butterfly leg and rotate under opponent, lift opponent\'s legs and roll to left side for sweep, finish straight foot lock',
                    'Butterfly ashi standing opponent left side, grip lapel, opponent breaks grip and grabs sleeve, pummel for wrist grip, establish half day la heeva, right leg behind opponent\'s left knee, sweep, finish day la heeva straight foot lock',
                    'Butterfly ashi standing opponent left side, grip lapel, opponent breaks grip and grabs sleeve, pummel for wrist grip, establish half day la heeva, right leg behind opponent\'s left knee, sweep, finish butterfly ashi straight foot lock',
                    'Butterfly ashi standing opponent right side, switch to kay guard, off-balance opponent away, finish knee bar',
                    'Butterfly ashi standing opponent left side, switch to kay guard, off-balance opponent away, finish knee bar',
                    'Butterfly ashi seated opponent left side, finish outside straight foot lock',
                    'Butterfly ashi seated opponent left side, finish square straight foot lock',
                    'Butterfly ashi seated opponent left side, finish inside straight foot lock',
                    'Butterfly ashi seated opponent left side, base on head, finish belly down straight foot lock',
                    'Butterfly ashi seated opponent right side, finish outside straight foot lock',
                    'Butterfly ashi seated opponent right side, finish square straight foot lock',
                    'Butterfly ashi seated opponent right side, finish inside straight foot lock',
                    'Butterfly ashi seated opponent right side, base on head, finish belly down straight foot lock',
                    'Butterfly ashi seated opponent right side, post and come up to finish knee bar',
                    'Butterfly ashi seated opponent left side, post and come up to finish knee bar'
                    'Butterfly ashi seated opponent right side, double elbow grip, finish Aoki lock',
                    'Butterfly ashi seated opponent left side, double elbow grip, finish Aoki lock',
                    'Zee guard right side, opponent attempts hip switch, catch on frames, push opponent away to right, cross legs over their back, finish knee bar',
                    'Zee guard left side, opponent attempts hip switch, catch on frames, push opponent away to left, cross legs over their back, finish knee bar',
                    'Day la heeva seated opponent left side, opponent opens leg out, post on hip and up on bottom knee, finish day la heeva straight footlock',
                    'Day la heeva seated opponent right side, opponent opens leg out, post on hip and up on bottom knee, finish day la heeva straight footlock'],     # Offense blitz, leg locks
                    2:
                    ['Back control, fall to right side, finish arm bar',
                    'Back control, fall to left side, finish arm bar',
                    'Leg ride right side, finish arm bar',
                    'Leg ride left side, finish arm bar',
                    'Knee on belly top standard right side, finish far side arm bar',
                    'Knee on belly top standard left side, finish far side arm bar',
                    'Knee on belly top standard right side, finish near side arm bar',
                    'Knee on belly top standard left side, finish near side arm bar',
                    'Zee guard right side, opponent overextends their right arm, establish shoulder crunch, bring right leg over crunched shoulder, finish arm bar over right hip',
                    'Zee guard right side, opponent overextends their right arm, establish shoulder crunch, bring right leg over crunched shoulder, opponent rolls, finish arm bar over right hip',
                    'Zee guard right side, right hand grip behind same side arm pit, bring legs through and over, back heel feet to butt and cross feet, finish arm bar',
                    'Zee guard right side, right hand grip behind same side arm pit, bring legs through and over, back heel feet to butt and cross feet, opponent rolls, finish arm bar',
                    'Zee guard right side, right hand grip behind same side arm pit, sit up to omoplata position, secure seat belt and finish omoplata',
                    'Zee guard right side, right hand grip behind same side arm pit, sit up to omoplata position, opponent rolls, follow roll, establish right hand scoop grip, finish omoplata',
                    'Zee guard right side, right hand grip behind same side arm pit, sit up to omoplata position, opponent rolls, follow roll, use left foot hook to establish right hand scoop grip, finish omoplata',
                    'Zee guard right side, right hand gently resting behind opponent\'s left elbow, opponent stands up, finish shotgun arm bar',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, opponent prevents kimura finish, come up to forehead and knees, strip the grip and finish left lat arm bar',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, opponent prevents kimura finish, come up to forehead and knees, opponent still keeps grip, roll to right hip to back, finish arm bar',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, feet together, finish arm bar over right hip',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, swing out right leg to over the right shoulder, feet together, finish arm bar over right hip',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, swing out right leg to over the right shoulder, feet together, opponent rolls, finish arm bar over right hip',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, opponent blocks right leg swing out, go alternate route to leg over right shoulder, feet together, opponent rolls finish arm bar over right hip',
                    'Zee guard left side, opponent overextends their left arm, establish shoulder crunch, bring left leg over crunched shoulder, finish arm bar over left hip',
                    'Zee guard left side, opponent overextends their left arm, establish shoulder crunch, bring left leg over crunched shoulder, opponent rolls, finish arm bar over left hip',
                    'Zee guard left side, left hand grip behind same side arm pit, bring legs through and over, back heel feet to butt and cross feet, finish arm bar',
                    'Zee guard left side, left hand grip behind same side arm pit, bring legs through and over, back heel feet to butt and cross feet, opponent rolls, finish arm bar',
                    'Zee guard left side, left hand grip behind same side arm pit, sit up to omoplata position, secure seat belt and finish omoplata',
                    'Zee guard left side, left hand grip behind same side arm pit, sit up to omoplata position, opponent rolls, follow roll, establish left hand scoop grip, finish omoplata',
                    'Zee guard left side, left hand grip behind same side arm pit, sit up to omoplata position, opponent rolls, follow roll, use right foot hook to establish left hand scoop grip, finish omoplata',
                    'Zee guard left side, left hand gently resting behind opponent\'s right elbow, opponent stands up, finish shotgun arm bar',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, opponent prevents kimura finish, come up to forehead and knees, strip the grip and finish right lat arm bar',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, opponent prevents kimura finish, come up to forehead and knees, opponent still keeps grip, roll to left hip to back, finish arm bar',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, feet together, finish arm bar over left hip',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, swing out left leg to over the left shoulder, feet together, finish arm bar over left hip',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, swing out left leg to over the left shoulder, feet together, opponent rolls, finish arm bar over left hip',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, opponent blocks left leg swing out, go alternate route to leg over left shoulder, feet together, opponent rolls finish arm bar over left hip'],     # Offense blitz, arm locks
                    3:
                    ['Back control fall to right side, finish right arm rear-naked-choke',
                    'Back control fall to right side, transition to arm bar position, transition back to back control, finish right arm rear-naked-choke',
                    'Back control fall to left side, finish left arm rear-naked-choke',
                    'Back control fall to left side, transition to arm bar position, transition back to back control, finish left arm rear-naked-choke',
                    'Leg ride leg between right side, finish arm triangle',
                    'Leg ride leg between right side, finish arm-in ezekiel',
                    'Leg ride leg between right side, Dag estani grip, roll opponent to belly, finish rear naked choke',
                    'Leg ride leg between left side, finish arm triangle',
                    'Leg ride leg between left side, finish arm-in ezekiel',
                    'Leg ride leg between left side, Dag estani grip, roll opponent to belly, finish rear naked choke',
                    'Leg ride right side, finish arm triangle',
                    'Leg ride right side, finish arm-in ezekiel',
                    'Leg ride left side, finish arm triangle',
                    'Leg ride left side, finish arm-in ezekiel',
                    'Zee guard right side, opponent overextends their right arm, establish shoulder crunch, right knee to opponent\'s left shoulder, opponent grabs right thigh with their left hand, place left foot on hip, break leg grip, finish triangle strangle',
                    'Zee guard right side, strong subtle Zee guard setup, opponent trys to pressure in, use frames to create space and lock up triangle strangle finish',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, opponent prevents kimura finish, come up to forehead and knees, right leg under, left leg over, finish achilles triangle strangle',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, opponent prevents kimura finish, come up to forehead and knees, right leg under, left leg over, opponent pressures into you, finish front triangle strangle',
                    'Zee guard right side, opponent attempts weave pass with left arm without knee passing through, right hand grip behind weave arm arm pit, left hand grip far wrist, scissor legs to break weave, finish triangle strangle',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to heavy on opponent\'s back, shoot lower leg through gap and lock up legs, climb for height and finish yoko ono triangle strangle',
                    'Zee guard left side, opponent overextends their left arm, establish shoulder crunch, left knee to opponent\'s right shoulder, opponent grabs left thigh with their right hand, place right foot on hip, break leg grip, finish triangle strangle',
                    'Zee guard left side, strong subtle Zee guard setup, opponent trys to pressure in, use frames to create space and lock up triangle strangle finish',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, opponent prevents kimura finish, come up to forehead and knees, left leg under, right leg over, finish achilles triangle strangle',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, opponent prevents kimura finish, come up to forehead and knees, left leg under, right leg over, opponent pressures into you, finish front triangle strangle',
                    'Zee guard left side, opponent attempts weave pass with right arm without knee passing through, left hand grip behind weave arm arm pit, right hand grip far wrist, scissor legs to break weave, finish triangle strangle',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to heavy on opponent\'s back, shoot lower leg through gap and lock up legs, climb for height and finish yoko ono triangle strangle'],     # Offense blitz, strangles
                    4:
                    ['Zee guard right side, establish kimura grip on opponent\'s right arm, opponent postures up to break grip, shoulder and head post with scoop grip, post and pull under into single leg X position',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, opponent postures up to break grip, shoulder and head post with scoop grip, post and pull under into single leg X position',
                    'Day la heeva seated opponent right side, bolo into back take',
                    'Day la heeva seated opponent left side, bolo into back take',
                    'Half guard bottom left side, inside knee down, under the shin, left hand under hook, opponent secures whizzer, attempt roll under to deep half guard, opponent bases out hands, get height to body lock, take the back',
                    'Half guard bottom left side, inside knee down, under the shin, left hand under hook, opponent secures heavy whizzer, grip behind opponent\'s thigh, up into dog fight position, push opponent\'s face, hop around to far side, take the back',
                    'Half guard bottom left side, inside knee down, under the shin, left hand under hook, opponent secures heavy whizzer, grip behind opponent\'s thigh, up into dog fight position, opponent is heavy with the whizzer, limp arm out, take the back',
                    'Half guard bottom right side, inside knee down, under the shin, right hand under hook, opponent secures whizzer, attempt roll under to deep half guard, opponent bases out hands, get height to body lock, take the back',
                    'Half guard bottom right side, inside knee down, under the shin, right hand under hook, opponent secures heavy whizzer, grip behind opponent\'s thigh, up into dog fight position, push opponent\'s face, hop around to far side, take the back',
                    'Half guard bottom right side, inside knee down, under the shin, right hand under hook, opponent secures heavy whizzer, grip behind opponent\'s thigh, up into dog fight position, opponent is heavy with the whizzer, limp arm out, take the back',
                    'Reverse Zee guard right side, opponent\'s left arm over your shoulder, right hand far trap grip, left hand chin-strap, roll over sweep to left',
                    'Reverse Zee guard left side, opponent\'s right arm over your shoulder, left hand far trap grip, right hand chin-strap, roll over sweep to right',
                    'Half guard bottom right side, inside knee down, complete knee lever sweep',
                    'Half guard bottom left side, inside knee down, complete knee lever sweep',
                    'Zee guard right side, opponent attempts hip switch, finish sweep',
                    'Zee guard left side, opponent attempts hip switch, finish sweep',
                    'Seated guard standing opponent left side, inside knee pull to single leg take down', 
                    'Seated guard standing opponent left side, attempted arm drag, inside achilles grab to single leg take down',
                    'Seated guard standing opponent right side, inside knee pull to single leg take down', 
                    'Seated guard standing opponent right side, attempted arm drag, inside achilles grab to single leg take down',
                    'Seated guard standing opponent right side, criss-cross double outside knee pull, finish side take down',
                    'Seated guard standing opponent left side, criss-cross double outside knee pull, finish side take down',
                    'Half guard bottom right side, inside knee up, hands to near side armpit, foot butterfly hook, extend and finish take down',
                    'Half guard bottom left side, inside knee up, hands to near side armpit, foot butterfly hook, extend and finish take down',
                    'Standing, standing opponent right side, left hand collar tie and elbow grip, change levels finish single leg take down',
                    'Standing, standing opponent right side, left hand collar tie and elbow grip, finish right side foot sweep',
                    'Standing, standing opponent left side, right hand collar tie and elbow grip, change levels finish single leg take down',
                    'Standing, standing opponent left side, right hand collar tie and elbow grip, finish left side foot sweep',
                    'Standing, standing opponent right side, opponent has head inside body lock, finish harai goshi throw',
                    'Standing, standing opponent left side, opponent has head inside body lock, finish harai goshi throw',
                    'Standing, standing opponent right side, opponent has head outside body lock, finish harai goshi throw',
                    'Standing, standing opponent left side, opponent has head outside body lock, finish harai goshi throw',
                    'Standing, standing opponent, right side whizzer, finish leg between uchi mata take down',
                    'Standing, standing opponent, left side whizzer, finish leg between uchi mata take down',
                    'Standing, supine opponent right side, stinky feet to reverse knee on belly',
                    'Standing, supine opponent left side, stinky feet to reverse knee on belly',
                    'Standing, supine opponent right side, stinky feet to knee on belly',
                    'Standing, supine opponent left side, stinky feet to knee on belly',
                    'Standing, supine opponent, opponent overextends legs, pull and rotate them to right',
                    'Standing, supine opponent, opponent overextends legs, pull and rotate them to left',
                    'Standing, supine opponent right side, bait toriondo pass, finish leg drag',
                    'Standing, supine opponent left side, bait toriondo pass, finish leg drag',
                    'Day la heeva guard standing opponent right side, circle around and take the back',
                    'Day la heeva guard standing opponent right side, circle around and take the back',
                    'Day la heeva guard standing opponent right side, attempting circle to back, opponent avoids and stays square, extend hook behind far knee, rotate into deep half guard-like position, push away with feet, stand and take the back',
                    'Day la heeva guard standing opponent left side, attempting circle to back, opponent avoids and stays square, extend hook behind far knee, rotate into deep half guard-like position, push away with feet, stand and take the back',
                    'Reverse day la heeva kneeling opponent right side, knee through, right foot push near armpit, left hand lift near heel, invert under leg to take the back',
                    'Reverse day la heeva kneeling opponent left side, knee through, left foot push near armpit, right hand lift near heel, invert under leg to take the back'],     # Offense blitz, positional advancements
                    5:
                    ['Zee guard right side, establish kimura grip on opponent\'s right arm, opponent postures up to break grip, shoulder and head post with scoop grip, post and pull under into single leg X position',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, opponent postures up to break grip, shoulder and head post with scoop grip, post and pull under into single leg X position',
                    'Day la heeva seated opponent right side, bolo into back take',
                    'Day la heeva seated opponent left side, bolo into back take',
                    'Half guard bottom left side, inside knee down, under the shin, left hand under hook, opponent secures whizzer, attempt roll under to deep half guard, opponent bases out hands, get height to body lock, take the back',
                    'Half guard bottom left side, inside knee down, under the shin, left hand under hook, opponent secures heavy whizzer, grip behind opponent\'s thigh, up into dog fight position, push opponent\'s face, hop around to far side, take the back',
                    'Half guard bottom left side, inside knee down, under the shin, left hand under hook, opponent secures heavy whizzer, grip behind opponent\'s thigh, up into dog fight position, opponent is heavy with the whizzer, limp arm out, take the back',
                    'Half guard bottom right side, inside knee down, under the shin, right hand under hook, opponent secures whizzer, attempt roll under to deep half guard, opponent bases out hands, get height to body lock, take the back',
                    'Half guard bottom right side, inside knee down, under the shin, right hand under hook, opponent secures heavy whizzer, grip behind opponent\'s thigh, up into dog fight position, push opponent\'s face, hop around to far side, take the back',
                    'Half guard bottom right side, inside knee down, under the shin, right hand under hook, opponent secures heavy whizzer, grip behind opponent\'s thigh, up into dog fight position, opponent is heavy with the whizzer, limp arm out, take the back',
                    'Reverse Zee guard right side, opponent\'s left arm over your shoulder, right hand far trap grip, left hand chin-strap, roll over sweep to left',
                    'Reverse Zee guard left side, opponent\'s right arm over your shoulder, left hand far trap grip, right hand chin-strap, roll over sweep to right',
                    'Half guard bottom right side, inside knee down, complete knee lever sweep',
                    'Half guard bottom left side, inside knee down, complete knee lever sweep',
                    'Zee guard right side, opponent attempts hip switch, finish sweep',
                    'Zee guard left side, opponent attempts hip switch, finish sweep',
                    'Seated guard standing opponent left side, inside knee pull to single leg take down', 
                    'Seated guard standing opponent left side, attempted arm drag, inside achilles grab to single leg take down',
                    'Seated guard standing opponent right side, inside knee pull to single leg take down', 
                    'Seated guard standing opponent right side, attempted arm drag, inside achilles grab to single leg take down',
                    'Seated guard standing opponent right side, criss-cross double outside knee pull, finish side take down',
                    'Seated guard standing opponent left side, criss-cross double outside knee pull, finish side take down',
                    'Half guard bottom right side, inside knee up, hands to near side armpit, foot butterfly hook, extend and finish take down',
                    'Half guard bottom left side, inside knee up, hands to near side armpit, foot butterfly hook, extend and finish take down',
                    'Standing, standing opponent right side, left hand collar tie and elbow grip, change levels finish single leg take down',
                    'Standing, standing opponent right side, left hand collar tie and elbow grip, finish right side foot sweep',
                    'Standing, standing opponent left side, right hand collar tie and elbow grip, change levels finish single leg take down',
                    'Standing, standing opponent left side, right hand collar tie and elbow grip, finish left side foot sweep',
                    'Standing, standing opponent right side, opponent has head inside body lock, finish harai goshi throw',
                    'Standing, standing opponent left side, opponent has head inside body lock, finish harai goshi throw',
                    'Standing, standing opponent right side, opponent has head outside body lock, finish harai goshi throw',
                    'Standing, standing opponent left side, opponent has head outside body lock, finish harai goshi throw',
                    'Standing, standing opponent, right side whizzer, finish leg between uchi mata take down',
                    'Standing, standing opponent, left side whizzer, finish leg between uchi mata take down',
                    'Standing, supine opponent right side, stinky feet to reverse knee on belly',
                    'Standing, supine opponent left side, stinky feet to reverse knee on belly',
                    'Standing, supine opponent right side, stinky feet to knee on belly',
                    'Standing, supine opponent left side, stinky feet to knee on belly',
                    'Standing, supine opponent, opponent overextends legs, pull and rotate them to right',
                    'Standing, supine opponent, opponent overextends legs, pull and rotate them to left',
                    'Standing, supine opponent right side, bait toriondo pass, finish leg drag',
                    'Standing, supine opponent left side, bait toriondo pass, finish leg drag',
                    'Standing, supine opponent right side, failed backstep attempt, hop over to other leg, finish knee bar',
                    'Standing, supine opponent left side, failed backstep attempt, hop over to other leg, finish knee bar',
                    'Day la heeva guard standing opponent right side, circle around and take the back',
                    'Day la heeva guard standing opponent right side, circle around and take the back',
                    'Day la heeva guard standing opponent right side, attempting circle to back, opponent avoids and stays square, extend hook behind far knee, rotate into deep half guard-like position, push away with feet, stand and take the back',
                    'Day la heeva guard standing opponent left side, attempting circle to back, opponent avoids and stays square, extend hook behind far knee, rotate into deep half guard-like position, push away with feet, stand and take the back',
                    'Reverse day la heeva kneeling opponent right side, knee through, right foot push near armpit, left hand lift near heel, invert under leg to take the back',
                    'Reverse day la heeva kneeling opponent left side, knee through, left foot push near armpit, right hand lift near heel, invert under leg to take the back',
                    'Back control fall to right side, finish right arm rear-naked-choke',
                    'Back control fall to right side, transition to arm bar position, transition back to back control, finish right arm rear-naked-choke',
                    'Back control fall to left side, finish left arm rear-naked-choke',
                    'Back control fall to left side, transition to arm bar position, transition back to back control, finish left arm rear-naked-choke',
                    'Leg ride leg between right side, finish arm triangle',
                    'Leg ride leg between right side, finish arm-in ezekiel',
                    'Leg ride leg between right side, Dag estani grip, roll opponent to belly, finish rear naked choke',
                    'Leg ride leg between left side, finish arm triangle',
                    'Leg ride leg between left side, finish arm-in ezekiel',
                    'Leg ride leg between left side, Dag estani grip, roll opponent to belly, finish rear naked choke',
                    'Leg ride right side, finish arm triangle',
                    'Leg ride right side, finish arm-in ezekiel',
                    'Leg ride left side, finish arm triangle',
                    'Leg ride left side, finish arm-in ezekiel',
                    'Zee guard right side, opponent overextends their right arm, establish shoulder crunch, right knee to opponent\'s left shoulder, opponent grabs right thigh with their left hand, place left foot on hip, break leg grip, finish triangle strangle',
                    'Zee guard right side, strong subtle Zee guard setup, opponent trys to pressure in, use frames to create space and lock up triangle strangle finish',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, opponent prevents kimura finish, come up to forehead and knees, right leg under, left leg over, finish achilles triangle strangle',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, opponent prevents kimura finish, come up to forehead and knees, right leg under, left leg over, opponent pressures into you, finish front triangle strangle',
                    'Zee guard right side, opponent attempts weave pass with left arm without knee passing through, right hand grip behind weave arm arm pit, left hand grip far wrist, scissor legs to break weave, finish triangle strangle',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to heavy on opponent\'s back, shoot lower leg through gap and lock up legs, climb for height and finish yoko ono triangle strangle',
                    'Zee guard left side, opponent overextends their left arm, establish shoulder crunch, left knee to opponent\'s right shoulder, opponent grabs left thigh with their right hand, place right foot on hip, break leg grip, finish triangle strangle',
                    'Zee guard left side, strong subtle Zee guard setup, opponent trys to pressure in, use frames to create space and lock up triangle strangle finish',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, opponent prevents kimura finish, come up to forehead and knees, left leg under, right leg over, finish achilles triangle strangle',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, opponent prevents kimura finish, come up to forehead and knees, left leg under, right leg over, opponent pressures into you, finish front triangle strangle',
                    'Zee guard left side, opponent attempts weave pass with right arm without knee passing through, left hand grip behind weave arm arm pit, right hand grip far wrist, scissor legs to break weave, finish triangle strangle',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to heavy on opponent\'s back, shoot lower leg through gap and lock up legs, climb for height and finish yoko ono triangle strangle',
                    'Back control, fall to right side, finish arm bar',
                    'Back control, fall to left side, finish arm bar',
                    'Leg ride right side, finish arm bar',
                    'Leg ride left side, finish arm bar',
                    'Knee on belly top standard right side, finish far side arm bar',
                    'Knee on belly top standard left side, finish far side arm bar',
                    'Knee on belly top standard right side, finish near side arm bar',
                    'Knee on belly top standard left side, finish near side arm bar',
                    'Zee guard right side, opponent overextends their right arm, establish shoulder crunch, bring right leg over crunched shoulder, finish arm bar over right hip',
                    'Zee guard right side, opponent overextends their right arm, establish shoulder crunch, bring right leg over crunched shoulder, opponent rolls, finish arm bar over right hip',
                    'Zee guard right side, right hand grip behind same side arm pit, bring legs through and over, back heel feet to butt and cross feet, finish arm bar',
                    'Zee guard right side, right hand grip behind same side arm pit, bring legs through and over, back heel feet to butt and cross feet, opponent rolls, finish arm bar',
                    'Zee guard right side, right hand grip behind same side arm pit, sit up to omoplata position, secure seat belt and finish omoplata',
                    'Zee guard right side, right hand grip behind same side arm pit, sit up to omoplata position, opponent rolls, follow roll, establish right hand scoop grip, finish omoplata',
                    'Zee guard right side, right hand grip behind same side arm pit, sit up to omoplata position, opponent rolls, follow roll, use left foot hook to establish right hand scoop grip, finish omoplata',
                    'Zee guard right side, right hand gently resting behind opponent\'s left elbow, opponent stands up, finish shotgun arm bar',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, opponent prevents kimura finish, come up to forehead and knees, strip the grip and finish left lat arm bar',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, opponent prevents kimura finish, come up to forehead and knees, opponent still keeps grip, roll to right hip to back, finish arm bar',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, right leg to over the right shoulder, feet together, finish arm bar over right hip',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, swing out right leg to over the right shoulder, feet together, finish arm bar over right hip',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, swing out right leg to over the right shoulder, feet together, opponent rolls, finish arm bar over right hip',
                    'Zee guard right side, establish kimura grip on opponent\'s right arm, opponent blocks right leg swing out, go alternate route to leg over right shoulder, feet together, opponent rolls finish arm bar over right hip',
                    'Zee guard left side, opponent overextends their left arm, establish shoulder crunch, bring left leg over crunched shoulder, finish arm bar over left hip',
                    'Zee guard left side, opponent overextends their left arm, establish shoulder crunch, bring left leg over crunched shoulder, opponent rolls, finish arm bar over left hip',
                    'Zee guard left side, left hand grip behind same side arm pit, bring legs through and over, back heel feet to butt and cross feet, finish arm bar',
                    'Zee guard left side, left hand grip behind same side arm pit, bring legs through and over, back heel feet to butt and cross feet, opponent rolls, finish arm bar',
                    'Zee guard left side, left hand grip behind same side arm pit, sit up to omoplata position, secure seat belt and finish omoplata',
                    'Zee guard left side, left hand grip behind same side arm pit, sit up to omoplata position, opponent rolls, follow roll, establish left hand scoop grip, finish omoplata',
                    'Zee guard left side, left hand grip behind same side arm pit, sit up to omoplata position, opponent rolls, follow roll, use right foot hook to establish left hand scoop grip, finish omoplata',
                    'Zee guard left side, left hand gently resting behind opponent\'s right elbow, opponent stands up, finish shotgun arm bar',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, opponent prevents kimura finish, come up to forehead and knees, strip the grip and finish right lat arm bar',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, opponent prevents kimura finish, come up to forehead and knees, opponent still keeps grip, roll to left hip to back, finish arm bar',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, left leg to over the left shoulder, feet together, finish arm bar over left hip',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, swing out left leg to over the left shoulder, feet together, finish arm bar over left hip',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, swing out left leg to over the left shoulder, feet together, opponent rolls, finish arm bar over left hip',
                    'Zee guard left side, establish kimura grip on opponent\'s left arm, opponent blocks left leg swing out, go alternate route to leg over left shoulder, feet together, opponent rolls finish arm bar over left hip',
                    'Seated guard standing opponent, left side, inside knee pull, finish knee bar', 
                    'Seated guard standing opponent, right side, scoot under, sweep to footlock finish',
                    'Seated guard standing opponent, right side, inside knee pull, finish knee bar', 
                    'Seated guard standing opponent, left side, scoot under, sweep to footlock finish',
                    'Seated guard kneeling opponent, right side, hand to same-side shoulder, hop out to side with leg between opponent, invert and roll through finish knee bar',
                    'Seated guard kneeling opponent, right side, hand to same-side shoulder, hop out to side with leg between opponent, invert, roll back into opponents\'s legs, finish knee bar',
                    'Seated guard kneeling opponent, left side, hand to same-side shoulder, hop out to side with leg between opponent, invert and roll through finish knee bar',
                    'Seated guard kneeling opponent, left side, hand to same-side shoulder, hop out to side with leg between opponent, invert, roll back into opponents\'s legs, finish knee bar',
                    'Reverse Zee guard right side, finish early entry knee bar', 
                    'Reverse Zee guard right side, finish late entry knee bar',
                    'Reverse Zee guard left side, finish early entry knee bar', 
                    'Reverse Zee guard left side, finish late entry knee bar',
                    'Half guard bottom right side, inside knee up, hands to near side armpit, foot butterfly hook, extend and finish knee bar',
                    'Half guard bottom left side, inside knee up, hands to near side armpit, foot butterfly hook, extend and finish knee bar',
                    'Standing, supine opponent right side, backstep to knee bar finish',
                    'Standing, supine opponent right side, backstep to far leg footlock finish',
                    'Standing, supine opponent right side, sit down into straight footlock finish option 1',
                    'Standing, supine opponent right side, sit down into straight footlock finish upright option 2',
                    'Standing, supine opponent right side, sit down into straight footlock main finish option 3',
                    'Standing, supine opponent right side, sit down into straight footlock, transition to knee bar finish',
                    'Standing, supine opponent left side, backstep to knee bar finish',
                    'Standing, supine opponent left side, backstep to knee bar finish',
                    'Standing, supine opponent left side, backstep to far leg footlock finish',
                    'Standing, supine opponent left side, sit down into straight footlock finish option 1',
                    'Standing, supine opponent left side, sit down into straight footlock finish upright option 2',
                    'Standing, supine opponent left side, sit down into straight footlock main finish option 3',
                    'Standing, supine opponent left side, sit down into straight footlock, transition to knee bar finish',
                    'Turtle guard square rear body lock right side, over wrap leg, roll to same side, secure opponent\'s top leg for knee bar finish',
                    'Turtle guard square rear body lock left side, over wrap leg, roll to same side, secure opponent\'s top leg for knee bar finish',
                    'Turtle guard leg between rear body lock right side, roll over inside shoulder, finish knee bar',
                    'Turtle guard leg between rear body lock left side, roll over inside shoulder, finish knee bar',
                    'Fifty fifty guard left side, sit up full spin through option, finish knee bar',
                    'Fifty fifty guard right side, sit up full spin through option, finish knee bar',
                    'Fifty fifty guard left side, sit up to double leg control option, finish knee bar',
                    'Fifty fifty guard right side, sit up to double leg control option, finish knee bar',
                    'Fifty fifty guard left side, slide inside knee back, finish sheer knee bar',
                    'Fifty fifty guard right side, slide inside knee back, finish sheer knee bar',
                    'Deep half guard right side, flare opponent\'s leg out and square hips, bridge up finish dog bar',
                    'Deep half guard left side, flare opponent\'s leg out and square hips, bridge up finish dog bar',
                    'Knee shield bottom right side, kick right leg onto far side, opponent sits to their outside hip, finish knee bar',
                    'Knee shield bottom left side, kick left leg onto far side, opponent sits to their outside hip, finish knee bar',
                    'Knee shield bottom right side, kick right leg onto far side, opponent rolls over their right shoulder, finish knee bar',
                    'Knee shield bottom left side, kick left leg onto far side, opponent rolls over their left shoulder, finish knee bar',
                    'Half guard top right side, knee slide full rotation, finish knee bar',
                    'Half guard top left side, knee slide full rotation, finish knee bar',
                    'Half guard top right side, knee slide and post, opponent turns away, finish double leg control knee bar',
                    'Half guard top left side, knee slide and post, opponent turns away, finish double leg control knee bar',
                    'Leg drag left side, windshield-wipe feet, step over and fall to left side, finish lat knee bar',
                    'Leg drag left side, windshield-wipe feet, swing leg all the way through falling to right side, finish lat knee bar',
                    'Leg drag right side, windshield-wipe feet, step over and fall to right side, finish lat knee bar',
                    'Leg drag right side, windshield-wipe feet, swing leg all the way through falling to left side, finish lat knee bar',
                    'Knee on belly top reverse position left side, knee through to foot, roll to left side finish right lat knee bar',
                    'Knee on belly top reverse position right side, knee through to foot, roll to right side finish left lat knee bar',
                    'Butterfly ashi standing opponent right side, grip lapel, sweep to right side, finish straight foot lock',
                    'Butterfly ashi standing opponent right side, grip lapel, opponent breaks grip, double leg sweep, finish straight foot lock',
                    'Butterfly ashi standing opponent right side, opponent posts hands to left side, swing butterfly leg and rotate under opponent, lift opponent\'s legs and roll to right side for sweep, finish straight foot lock',
                    'Butterfly ashi standing opponent right side, grip lapel, opponent breaks grip and grabs sleeve, pummel for wrist grip, establish half day la heeva, left leg behind opponent\'s right knee, sweep, finish day la heeva straight foot lock',
                    'Butterfly ashi standing opponent right side, grip lapel, opponent breaks grip and grabs sleeve, pummel for wrist grip, establish half day la heeva, left leg behind opponent\'s right knee, sweep, finish butterfly ashi straight foot lock',
                    'Butterfly ashi standing opponent left side, grip lapel, sweep to left side, finish straight foot lock',
                    'Butterfly ashi standing opponent left side, grip lapel, opponent breaks grip, double leg sweep, finish straight foot lock',
                    'Butterfly ashi standing opponent left side, opponent posts hands to right side, swing butterfly leg and rotate under opponent, lift opponent\'s legs and roll to left side for sweep, finish straight foot lock',
                    'Butterfly ashi standing opponent left side, grip lapel, opponent breaks grip and grabs sleeve, pummel for wrist grip, establish half day la heeva, right leg behind opponent\'s left knee, sweep, finish day la heeva straight foot lock',
                    'Butterfly ashi standing opponent left side, grip lapel, opponent breaks grip and grabs sleeve, pummel for wrist grip, establish half day la heeva, right leg behind opponent\'s left knee, sweep, finish butterfly ashi straight foot lock',
                    'Butterfly ashi standing opponent right side, switch to kay guard, off-balance opponent away, finish knee bar',
                    'Butterfly ashi standing opponent left side, switch to kay guard, off-balance opponent away, finish knee bar',
                    'Butterfly ashi seated opponent left side, finish outside straight foot lock',
                    'Butterfly ashi seated opponent left side, finish square straight foot lock',
                    'Butterfly ashi seated opponent left side, finish inside straight foot lock',
                    'Butterfly ashi seated opponent left side, base on head, finish belly down straight foot lock',
                    'Butterfly ashi seated opponent right side, finish outside straight foot lock',
                    'Butterfly ashi seated opponent right side, finish square straight foot lock',
                    'Butterfly ashi seated opponent right side, finish inside straight foot lock',
                    'Butterfly ashi seated opponent right side, base on head, finish belly down straight foot lock',
                    'Butterfly ashi seated opponent right side, double elbow grip, finish Aoki lock',
                    'Butterfly ashi seated opponent left side, double elbow grip, finish Aoki lock',
                    'Butterfly ashi seated opponent right side, post and come up to finish knee bar',
                    'Butterfly ashi seated opponent left side, post and come up to finish knee bar',
                    'Zee guard right side, opponent attempts hip switch, catch on frames, push opponent away to right, cross legs over their back, finish knee bar',
                    'Zee guard left side, opponent attempts hip switch, catch on frames, push opponent away to left, cross legs over their back, finish knee bar',
                    'Day la heeva seated opponent left side, opponent opens leg out, post on hip and up on bottom knee, finish day la heeva straight footlock',
                    'Day la heeva seated opponent right side, opponent opens leg out, post on hip and up on bottom knee, finish day la heeva straight footlock']     # Offense blitz, ALL offense moves
                    },
                2: {1: None},   # Defense blitz to be built out in v2.0
                3: {1:
                    [None],     # Offense & defense blitz, leg locks
                    2:
                    [None],     # Offense & defense blitz, arm locks
                    3:
                    [],     # Offense & defense blitz, strangles
                    4:
                    [],     # Offense & defense blitz, passing
                    5:
                    []     # Offense & defense blitz, ALL offense moves
                    }
                }