
"use strict";

let StopController = require('./StopController.js')
let SetTorqueLimit = require('./SetTorqueLimit.js')
let SetSpeed = require('./SetSpeed.js')
let SetCompliancePunch = require('./SetCompliancePunch.js')
let SetComplianceMargin = require('./SetComplianceMargin.js')
let SetComplianceSlope = require('./SetComplianceSlope.js')
let TorqueEnable = require('./TorqueEnable.js')
let StartController = require('./StartController.js')
let RestartController = require('./RestartController.js')

module.exports = {
  StopController: StopController,
  SetTorqueLimit: SetTorqueLimit,
  SetSpeed: SetSpeed,
  SetCompliancePunch: SetCompliancePunch,
  SetComplianceMargin: SetComplianceMargin,
  SetComplianceSlope: SetComplianceSlope,
  TorqueEnable: TorqueEnable,
  StartController: StartController,
  RestartController: RestartController,
};
