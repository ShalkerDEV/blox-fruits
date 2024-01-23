getgenv().SpamSkill = false
getgenv().AutoUseRaceV3 = true
getgenv().Invisible = true
getgenv().InCombatNoReset = false
getgenv().Team = "Pirates" -- Marines
getgenv().TweenSpeed = 300 -- 350 max or Get Tp Back
 getgenv().Setting = { -- Select Weapon, Self Explain
        ["Melee"] = {["Enable"] = true,["Delay"] = 3,
          ["Skills"] = {
            ["Z"] = {["Enable"] = true,["HoldTime"] = 0,["TimeToNextSkill"] = 0,},
            [ "X"] = {["Enable"] = true,["HoldTime"] = 0, ["TimeToNextSkill"] = 0,},
            ["C"] = {["Enable"] = true,["HoldTime"] = 0, ["TimeToNextSkill"] = 0,},
            },
        },
        ["Sword"] = { ["Enable"] = true, ["Delay"] = 2,
            ["Skills"] = {
                ["Z"] = {["Enable"] = true,  ["HoldTime"] = 0.5,["TimeToNextSkill"] = 0,},
                ["X"] = {["Enable"] = true, ["HoldTime"] = 0.5, ["TimeToNextSkill"] = 0,},
            },
        },
    
    }