/**
 * =====================================================
 * AI Empire Pro V8
 * Test Runner
 * Datei: tests/run.js
 * =====================================================
 */

const assert = require("assert");

const Helpers = require("../server/utils/helpers");
const Validator = require("../server/utils/validator");
const Formatter = require("../server/utils/formatter");
const Crypto = require("../server/utils/crypto");

let passed = 0;
let failed = 0;

function test(name, fn) {

    try {

        fn();

        console.log(`✓ ${name}`);

        passed++;

    }

    catch (error) {

        console.error(`✗ ${name}`);

        console.error(error.message);

        failed++;

    }

}

console.log("");
console.log("====================================");
console.log(" AI Empire Pro V8 Test Runner");
console.log("====================================");
console.log("");

test("UUID erzeugen", () => {

    const id = Helpers.uuid();

    assert.ok(id.length > 20);

});

test("Email Validator", () => {

    assert.strictEqual(

        Validator.email("test@example.com"),

        true

    );

});

test("Passwort Validator", () => {

    assert.strictEqual(

        Validator.password("12345678"),

        true

    );

});

test("Currency Formatter", () => {

    const value = Formatter.currency(100);

    assert.ok(value.length > 0);

});

test("SHA256 Hash", () => {

    const hash = Crypto.hash("AI Empire");

    assert.strictEqual(

        hash.length,

        64

    );

});

test("AES Encrypt/Decrypt", () => {

    const encrypted = Crypto.encrypt("Hallo");

    const decrypted = Crypto.decrypt(encrypted);

    assert.strictEqual(

        decrypted,

        "Hallo"

    );

});

console.log("");
console.log("====================================");
console.log(`Tests erfolgreich : ${passed}`);
console.log(`Tests fehlgeschlagen : ${failed}`);
console.log("====================================");

process.exit(failed ? 1 : 0);
