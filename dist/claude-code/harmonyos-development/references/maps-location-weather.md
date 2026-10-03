# Location, Weather, and Map Kit

## Contents
- Location Kit (geoLocationManager)
- Weather Service Kit — weather data API
- Map Kit — MapComponent

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `Location Kit, geoLocationManager, Weather Service Kit, Map Kit, MapComponent`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

## Location Kit (geoLocationManager)

```ts
import { geoLocationManager } from '@kit.LocationKit'

// Permission required: ohos.permission.APPROXIMATELY_LOCATION (user_grant)
// module.json5: reason + usedScene required

const pos = await geoLocationManager.getCurrentLocation({
  priority: geoLocationManager.LocationRequestPriority.FIRST_FIX,
  scenario: geoLocationManager.LocationRequestScenario.UNSET,
  timeoutMs: 10000
})

const addresses = await geoLocationManager.getAddressesFromLocation({
  latitude: pos.latitude,
  longitude: pos.longitude,
  maxItems: 1
})

// Build readable location string from GeoAddress fields:
// administrativeArea (省) → subAdministrativeArea (市) → locality (区) → subLocality → placeName
```


## Weather Service Kit — weather data API

> Requires `ohos.permission.LOCATION` (or `APPROXIMATELY_LOCATION`) if using device location.

```ts
import { weatherService } from '@kit.WeatherServiceKit';

const weatherRequest: weatherService.WeatherRequest = {
  location: { latitude: 39.9042, longitude: 116.4074 },   // Beijing
  limitedDatasets: [
    weatherService.Dataset.CURRENT,    // current conditions
    weatherService.Dataset.DAILY,      // daily forecast
    weatherService.Dataset.HOURLY,     // hourly forecast
    weatherService.Dataset.ALERTS,     // severe weather alerts
    weatherService.Dataset.INDICES,    // life indices (UV, air quality...)
    weatherService.Dataset.TIDES,      // coastal tides
    weatherService.Dataset.MINUTE,     // minute-level precipitation
  ],
};

try {
  const weather = await weatherService.getWeather(weatherRequest);
  // weather.currentWeather.temperature, .humidity, .conditionCode, ...
  // weather.dailyForecast?.days[] (each: tempMax/tempMin/precipitation/sunrise/sunset)
  // weather.hourlyForecast?.hours[]
  // weather.weatherAlerts?.alerts[] (severity, summary)
} catch (err) {
  console.error('Weather fetch failed:', err);
}
```


## Map Kit — MapComponent

```ts
import { mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MapPage {
  private mapOptions: mapCommon.MapOptions = {
    position: {
      target: { latitude: 39.9042, longitude: 116.4074 },  // Beijing
      zoom: 12
    }
  };
  private mapController?: map.MapComponentController;

  build() {
    Column() {
      MapComponent({
        mapOptions: this.mapOptions,
        mapCallback: (err, controller) => {
          if (!err) {
            this.mapController = controller;
            this.addMarker();
          }
        }
      }).width('100%').layoutWeight(1)
    }
  }

  private addMarker() {
    this.mapController?.addMarker({
      position: { latitude: 39.9042, longitude: 116.4074 },
      title: 'Tiananmen',
      snippet: 'Beijing city center'
    });
  }
}
```

Required permissions in `module.json5`: `ohos.permission.LOCATION` and `ohos.permission.APPROXIMATELY_LOCATION`.
