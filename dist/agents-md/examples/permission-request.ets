import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';

const PERMISSION: Permissions = 'ohos.permission.CAMERA';

export async function requestCameraPermission(context: common.UIAbilityContext): Promise<boolean> {
  const atManager = abilityAccessCtrl.createAtManager();
  const result = await atManager.requestPermissionsFromUser(context, [PERMISSION]);
  return result.authResults.length > 0 && result.authResults[0] === 0;
}
