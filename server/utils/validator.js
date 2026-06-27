/**
 * =====================================================
 * AI Empire Pro V8
 * Validation Utilities
 * Datei: server/utils/validator.js
 * =====================================================
 */

class Validator {

    static required(value) {

        return value !== undefined &&
               value !== null &&
               value !== "";

    }

    static email(email) {

        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/

            .test(email);

    }

    static username(username) {

        return /^[a-zA-Z0-9_-]{3,32}$/

            .test(username);

    }

    static password(password) {

        return (

            typeof password === "string" &&

            password.length >= 8

        );

    }

    static url(url) {

        try {

            new URL(url);

            return true;

        }

        catch {

            return false;

        }

    }

    static number(value) {

        return !isNaN(value);

    }

    static integer(value) {

        return Number.isInteger(

            Number(value)

        );

    }

    static boolean(value) {

        return (

            value === true ||

            value === false ||

            value === "true" ||

            value === "false"

        );

    }

    static min(value, length) {

        return String(value).length >= length;

    }

    static max(value, length) {

        return String(value).length <= length;

    }

    static between(value, min, max) {

        return (

            Number(value) >= min &&

            Number(value) <= max

        );

    }

    static oneOf(value, list = []) {

        return list.includes(value);

    }

    static object(value) {

        return (

            typeof value === "object" &&

            value !== null &&

            !Array.isArray(value)

        );

    }

    static array(value) {

        return Array.isArray(value);

    }

    static uuid(value) {

        return /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i

            .test(value);

    }

    static validate(data = {}, rules = {}) {

        const errors = {};

        for (const field in rules) {

            const value = data[field];

            const validators = rules[field];

            for (const validator of validators) {

                const valid = validator(value);

                if (!valid) {

                    errors[field] = true;

                    break;

                }

            }

        }

        return {

            valid:

                Object.keys(errors).length === 0,

            errors

        };

    }

}

module.exports = Validator;
