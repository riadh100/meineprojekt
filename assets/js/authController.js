/**
 * =====================================================
 * AI Empire Pro V8
 * Auth Controller
 * Datei: server/controllers/authController.js
 * =====================================================
 */

const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");

const User = require("../models/User");

const JWT_SECRET =
    process.env.JWT_SECRET || "AI_EMPIRE_SECRET";

class AuthController {

    async login(req, res) {

        try {

            const {

                username,

                password

            } = req.body;

            if (!username || !password) {

                return res.status(400).json({

                    success: false,

                    message: "Benutzername und Passwort erforderlich."

                });

            }

            const user = await User.findOne({

                username

            });

            if (!user) {

                return res.status(401).json({

                    success: false,

                    message: "Ungültige Zugangsdaten."

                });

            }

            const valid = await bcrypt.compare(

                password,

                user.password

            );

            if (!valid) {

                return res.status(401).json({

                    success: false,

                    message: "Ungültige Zugangsdaten."

                });

            }

            const token = jwt.sign(

                {

                    id: user._id,

                    username: user.username,

                    role: user.role

                },

                JWT_SECRET,

                {

                    expiresIn: "12h"

                }

            );

            return res.json({

                success: true,

                token,

                user: {

                    id: user._id,

                    username: user.username,

                    email: user.email,

                    role: user.role

                }

            });

        }

        catch(error){

            console.error(error);

            return res.status(500).json({

                success:false,

                message:"Serverfehler."

            });

        }

    }

    async register(req,res){

        try{

            const{

                username,

                email,

                password

            }=req.body;

            const exists=await User.findOne({

                $or:[

                    {username},

                    {email}

                ]

            });

            if(exists){

                return res.status(400).json({

                    success:false,

                    message:"Benutzer existiert bereits."

                });

            }

            const hash=await bcrypt.hash(password,10);

            const user=await User.create({

                username,

                email,

                password:hash,

                role:"admin"

            });

            return res.status(201).json({

                success:true,

                user

            });

        }

        catch(error){

            console.error(error);

            return res.status(500).json({

                success:false,

                message:"Registrierung fehlgeschlagen."

            });

        }

    }

    async me(req,res){

        return res.json({

            success:true,

            user:req.user

        });

    }

}

module.exports=new AuthController();
